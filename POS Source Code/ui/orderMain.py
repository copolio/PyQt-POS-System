# 주문
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui import refund, choosePayment
import admin

#주문 목록 모델
orderNo = 1
orderedItems = []
totalPrice = 0
orderModel = QtGui.QStandardItemModel()
orderModel.setHorizontalHeaderLabels(['No', '상품명', '수량', '금액'])

# QtDesigner를 통해 생성한 UI 폼
class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(740, 230, 751, 661))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.orderList = QtWidgets.QTableView(self.splitter_2)
        self.orderList.setMinimumSize(QtCore.QSize(0, 400))
        self.orderList.setMaximumSize(QtCore.QSize(16777215, 400))
        self.orderList.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.orderList.setObjectName("orderList")
        self.orderList.verticalHeader().setVisible(False)
        self.orderList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.orderList.resizeColumnsToContents()
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(120, 80))
        self.label_6.setMaximumSize(QtCore.QSize(120, 80))
        self.label_6.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.totalPriceBox = QtWidgets.QTextEdit(self.layoutWidget)
        self.totalPriceBox.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.totalPriceBox.setReadOnly(True)
        self.totalPriceBox.setMinimumSize(QtCore.QSize(400, 80))
        self.totalPriceBox.setMaximumSize(QtCore.QSize(400, 80))
        self.totalPriceBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.totalPriceBox.setObjectName("totalPriceBox")
        self.horizontalLayout_5.addWidget(self.totalPriceBox)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(150, 80))
        self.label_8.setMaximumSize(QtCore.QSize(20, 80))
        self.label_8.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.resetBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.resetBtn.setMinimumSize(QtCore.QSize(350, 100))
        self.resetBtn.setMaximumSize(QtCore.QSize(350, 100))
        self.resetBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
                                    "background-color: rgb(255, 160, 52);")
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout_6.addWidget(self.resetBtn)
        self.payBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.payBtn.setMinimumSize(QtCore.QSize(350, 100))
        self.payBtn.setMaximumSize(QtCore.QSize(350, 100))
        self.payBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
                                  "background-color: rgb(94, 180, 255);")
        self.payBtn.setObjectName("payBtn")
        self.horizontalLayout_6.addWidget(self.payBtn)
        self.productList = QtWidgets.QListView(Form)
        self.productList.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.productList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.productList.setGeometry(QtCore.QRect(10, 250, 700, 600))
        self.productList.setMinimumSize(QtCore.QSize(700, 600))
        self.productList.setMaximumSize(QtCore.QSize(700, 600))
        self.productList.setObjectName("productList")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 120, 1220, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sortByChickenBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.sortByChickenBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.sortByChickenBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.sortByChickenBtn.setStyleSheet("font: 75 35pt \"함초롬돋움\";\n"
                                            "background-color: rgb(252, 190, 113);")
        self.sortByChickenBtn.setObjectName("sortByChickenBtn")
        self.horizontalLayout_3.addWidget(self.sortByChickenBtn)
        self.sortByDrinkBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.sortByDrinkBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.sortByDrinkBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.sortByDrinkBtn.setStyleSheet("font: 75 35pt \"함초롬돋움\";\n"
                                          "background-color: rgb(85, 201, 234);")
        self.sortByDrinkBtn.setObjectName("sortByDrinkBtn")
        self.horizontalLayout_3.addWidget(self.sortByDrinkBtn)
        self.sortByOtherBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.sortByOtherBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.sortByOtherBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.sortByOtherBtn.setStyleSheet("font: 75 35pt \"함초롬돋움\";\n"
                                          "background-color: rgb(159, 217, 111);")
        self.sortByOtherBtn.setObjectName("sortByOtherBtn")
        self.horizontalLayout_3.addWidget(self.sortByOtherBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(8, 9, 1481, 102))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setMinimumSize(QtCore.QSize(140, 50))
        self.label.setMaximumSize(QtCore.QSize(120, 50))
        self.label.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.timeBox = QtWidgets.QTextEdit(self.layoutWidget3)
        self.timeBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeBox.setReadOnly(True)
        self.timeBox.setMinimumSize(QtCore.QSize(200, 50))
        self.timeBox.setMaximumSize(QtCore.QSize(200, 50))
        self.timeBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout.addWidget(self.timeBox)
        spacerItem1 = QtWidgets.QSpacerItem(200, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.refundBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.refundBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.refundBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.refundBtn.setFont(font)
        self.refundBtn.setStyleSheet("font: 75 30pt \"함초롬돋움\";\n"
                                     "background-color: rgb(255, 129, 112);")
        self.refundBtn.setObjectName("refundBtn")
        self.horizontalLayout.addWidget(self.refundBtn)
        self.admBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.admBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.admBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.admBtn.setStyleSheet("font: 75 30pt \"함초롬돋움\";\n"
                                  "background-color: rgb(126, 224, 170);")
        self.admBtn.setObjectName("admBtn")
        self.horizontalLayout.addWidget(self.admBtn)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "합계"))
        self.label_8.setText(_translate("Form", "원"))
        self.resetBtn.setText(_translate("Form", "초기화"))
        self.payBtn.setText(_translate("Form", "결제"))
        self.sortByChickenBtn.setText(_translate("Form", "치킨"))
        self.sortByDrinkBtn.setText(_translate("Form", "음료"))
        self.sortByOtherBtn.setText(_translate("Form", "기타"))
        self.label.setText(_translate("Form", "현재 시각: "))
        self.refundBtn.setText(_translate("Form", "환불"))
        self.admBtn.setText(_translate("Form", "관리"))

class OrderMain(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.sortByChickenBtn.clicked.connect(self.sortByChicken)
        self.sortByDrinkBtn.clicked.connect(self.sortByDrink)
        self.sortByOtherBtn.clicked.connect(self.sortByOther)
        self.productList.doubleClicked.connect(self.addOrder)
        self.resetBtn.clicked.connect(self.reset)
        self.orderList.setModel(orderModel)
        self.orderList.resizeColumnsToContents()
        self.totalPriceBox.setPlainText('{:,}'.format(totalPrice))
        self.refundBtn.clicked.connect(self.refundBtnClicked)
        self.payBtn.clicked.connect(self.pay)
        self.admBtn.clicked.connect(self.openAdmin)
        self.show()

    # 안내 메세지 창 팝업
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    # 현재 시각 출력 함수
    @pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour + ":" + min + ":" + sec)

    @pyqtSlot()
    def sortByChicken(self):
        model = QtGui.QStandardItemModel()
        model.clear()
        sql = "SELECT * FROM Product WHERE Category='치킨'"
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            data = c.fetchall()
            conn.close()
            for i in data:
                model.appendRow(QtGui.QStandardItem(str(i[1])))
            self.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @pyqtSlot()
    def sortByDrink(self):
        model = QtGui.QStandardItemModel()
        model.clear()
        sql = "SELECT * FROM Product WHERE Category='음료'"
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            data = c.fetchall()
            conn.close()
            for i in data:
                model.appendRow(QtGui.QStandardItem(str(i[1])))
            self.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @pyqtSlot()
    def sortByOther(self):
        model = QtGui.QStandardItemModel()
        model.clear()
        sql = "SELECT * FROM Product WHERE Category='기타'"
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            data = c.fetchall()
            conn.close()
            for i in data:
                model.appendRow(QtGui.QStandardItem(str(i[1])))
            self.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    # 주문
    @pyqtSlot(QModelIndex)
    def addOrder(self, index):
        global orderNo, orderedItems, totalPrice
        productName = index.data()
        sql = "SELECT Price FROM Product WHERE Name='%s'" % productName
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            data = c.fetchall()
            conn.close()
            price = int(data[0][0])
            if productName in orderedItems:
                orderRow = int(orderedItems.index(productName))
                orderQuantity = int(orderModel.index(orderRow, 2).data()) + 1
                orderModel.setItem(orderRow, 2, QtGui.QStandardItem('{:,}'.format(orderQuantity)))
                orderModel.setItem(orderRow, 3, QtGui.QStandardItem('{:,}'.format(orderQuantity * price)))
            else:
                orderedItems.append(productName)
                row = [QtGui.QStandardItem('{:,}'.format(orderNo)), QtGui.QStandardItem(productName),
                       QtGui.QStandardItem('1'), QtGui.QStandardItem('{:,}'.format(price))]
                orderModel.appendRow(row)
                orderNo += 1
            totalPrice += price
            self.orderList.resizeColumnsToContents()
            self.totalPriceBox.setPlainText('{:,}'.format(totalPrice))
            self.orderList.setModel(orderModel)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    # 주문 초기화
    @pyqtSlot()
    def reset(self):
        global orderNo, orderedItems, totalPrice
        orderNo = 1
        orderedItems = []
        totalPrice = 0
        orderModel.clear()
        orderModel.setHorizontalHeaderLabels(['No', '상품명', '수량', '금액'])
        self.orderList.setModel(orderModel)
        self.totalPriceBox.setPlainText(str(totalPrice))

    # 결제 수단 선택 화면 호출
    @pyqtSlot()
    def pay(self):
        global totalPrice, orderedItems
        if orderedItems == []:
            self.showMessageBox('오류', '결제할 품목이 없습니다')
            return False
        else:
            self.close()
            choosePayment.ChoosePayment(self)
            choosePayment.orderMain.totalPrice = totalPrice
            choosePayment.orderMain.orderModel = orderModel
            choosePayment.orderMain.orderedItems = orderedItems

    # 환불 창 호출
    @pyqtSlot()
    def refundBtnClicked(self):
        refund.Refund(self)
    
    # 관리자 인증 화면 호출
    def openAdmin(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = admin.AdminAuth()
        self.close()