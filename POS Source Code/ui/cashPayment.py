# 현금 결제
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui import orderMain, choosePayment
from ui.orderMain import *
import datetime
import sqlite3
import user

#현금 결제 및 시재 모델
cashReceived = ''
sql = "SELECT Total FROM Management WHERE ID = (SELECT MAX(ID) FROM Management)"
try:
    conn = sqlite3.connect("pos.db")
    c = conn.cursor()
    c.execute(sql)
    data = c.fetchall()
    currentCash = data[0][0]
    conn.close()
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])

# QtDesigner를 통해 생성한 UI 폼
class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 6, 1422, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(400, 100))
        self.timeLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.timeLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.timeBox.setStyleSheet("font: 75 30pt \"함초롬돋움\";")
        self.timeBox.setMinimumSize(QtCore.QSize(400, 100))
        self.timeBox.setMaximumSize(QtCore.QSize(400, 100))
        self.timeBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeBox.setReadOnly(True)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout_2.addWidget(self.timeBox)
        spacerItem = QtWidgets.QSpacerItem(200, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.goBackBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.goBackBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.goBackBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.goBackBtn.setFont(font)
        self.goBackBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";\n"
"background-color: rgb(255, 129, 112);")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(190, 180, 460, 631))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn9.setMinimumSize(QtCore.QSize(150, 150))
        self.btn9.setMaximumSize(QtCore.QSize(150, 150))
        self.btn9.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 0, 2, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn8.setMinimumSize(QtCore.QSize(150, 150))
        self.btn8.setMaximumSize(QtCore.QSize(150, 150))
        self.btn8.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 0, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn7.setMinimumSize(QtCore.QSize(150, 150))
        self.btn7.setMaximumSize(QtCore.QSize(150, 150))
        self.btn7.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 0, 0, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn4.setMinimumSize(QtCore.QSize(150, 150))
        self.btn4.setMaximumSize(QtCore.QSize(150, 150))
        self.btn4.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn5.setMinimumSize(QtCore.QSize(150, 150))
        self.btn5.setMaximumSize(QtCore.QSize(150, 150))
        self.btn5.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn2.setMinimumSize(QtCore.QSize(150, 150))
        self.btn2.setMaximumSize(QtCore.QSize(150, 150))
        self.btn2.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 2, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn6.setMinimumSize(QtCore.QSize(150, 150))
        self.btn6.setMaximumSize(QtCore.QSize(150, 150))
        self.btn6.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn1.setMinimumSize(QtCore.QSize(150, 150))
        self.btn1.setMaximumSize(QtCore.QSize(150, 150))
        self.btn1.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 2, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn3.setMinimumSize(QtCore.QSize(150, 150))
        self.btn3.setMaximumSize(QtCore.QSize(150, 150))
        self.btn3.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 2, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.splitter)
        self.btn0.setMinimumSize(QtCore.QSize(460, 150))
        self.btn0.setMaximumSize(QtCore.QSize(460, 150))
        self.btn0.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.btn0.setObjectName("btn0")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(707, 220, 691, 461))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.priceLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.priceLabel.setMinimumSize(QtCore.QSize(150, 100))
        self.priceLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.priceLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.priceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout_4.addWidget(self.priceLabel)
        self.priceBox = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.priceBox.setMinimumSize(QtCore.QSize(400, 100))
        self.priceBox.setMaximumSize(QtCore.QSize(400, 100))
        self.priceBox.setReadOnly(True)
        self.priceBox.setStyleSheet("font: 75 40pt \"함초롬돋움\";")
        self.priceBox.setObjectName("priceBox")
        self.horizontalLayout_4.addWidget(self.priceBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cashLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.cashLabel.setMinimumSize(QtCore.QSize(150, 100))
        self.cashLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.cashLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.cashLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cashLabel.setObjectName("cashLabel")
        self.horizontalLayout_5.addWidget(self.cashLabel)
        self.cashBox = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.cashBox.setMinimumSize(QtCore.QSize(400, 100))
        self.cashBox.setMaximumSize(QtCore.QSize(400, 100))
        self.cashBox.setReadOnly(True)
        self.cashBox.setStyleSheet("font: 75 40pt \"함초롬돋움\";")
        self.cashBox.setObjectName("cashBox")
        self.horizontalLayout_5.addWidget(self.cashBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.changeLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.changeLabel.setMinimumSize(QtCore.QSize(150, 100))
        self.changeLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.changeLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.changeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changeLabel.setObjectName("changeLabel")
        self.horizontalLayout_6.addWidget(self.changeLabel)
        self.changeBox = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.changeBox.setMinimumSize(QtCore.QSize(400, 100))
        self.changeBox.setMaximumSize(QtCore.QSize(400, 100))
        self.changeBox.setReadOnly(True)
        self.changeBox.setStyleSheet("font: 75 40pt \"함초롬돋움\";")
        self.changeBox.setObjectName("changeBox")
        self.horizontalLayout_6.addWidget(self.changeBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.payBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.payBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.payBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.payBtn.setFont(font)
        self.payBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";\n"
"background-color: rgb(170, 170, 127);")
        self.payBtn.setObjectName("payBtn")
        self.horizontalLayout_3.addWidget(self.payBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel.setText(_translate("Form", "현재 시각: "))
        self.goBackBtn.setText(_translate("Form", "돌아가기"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn3.setText(_translate("Form", "3"))
        self.btn0.setText(_translate("Form", "0"))
        self.priceLabel.setText(_translate("Form", "결제 금액"))
        self.cashLabel.setText(_translate("Form", "받은 금액"))
        self.changeLabel.setText(_translate("Form", "거스름돈"))
        self.payBtn.setText(_translate("Form", "결제하기"))


class CashPayment(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        global totalPrice
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.goBackBtn.clicked.connect(self.onGoBackBtnClicked)
        self.btn9.clicked.connect(self.onBtn9Clicked)
        self.btn8.clicked.connect(self.onBtn8Clicked)
        self.btn7.clicked.connect(self.onBtn7Clicked)
        self.btn6.clicked.connect(self.onBtn6Clicked)
        self.btn5.clicked.connect(self.onBtn5Clicked)
        self.btn4.clicked.connect(self.onBtn4Clicked)
        self.btn3.clicked.connect(self.onBtn3Clicked)
        self.btn2.clicked.connect(self.onBtn2Clicked)
        self.btn1.clicked.connect(self.onBtn1Clicked)
        self.btn0.clicked.connect(self.onBtn0Clicked)
        self.payBtn.clicked.connect(self.onPayBtnClicked)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.priceBox.setPlainText('{:,}'.format(orderMain.totalPrice))
        self.show()

    # 현재 시각 출력 함수
    @pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour + ":" + min + ":" + sec)

    # 0-9 숫자 버튼 클릭
    @pyqtSlot()
    def onBtn9Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'9'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn8Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'8'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn7Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'7'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn6Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'6'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn5Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'5'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn4Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'4'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn3Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'3'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn2Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'2'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn1Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'1'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))
    @pyqtSlot()
    def onBtn0Clicked(self):
        global cashReceived
        cashReceived = cashReceived+'0'
        self.cashBox.setPlainText('{:,}'.format(int(cashReceived)))

    # 현금 결제
    @pyqtSlot()
    def onPayBtnClicked(self):
        global cashReceived, totalPrice, currentCash
        now = datetime.datetime.now()
        NoSale = int(now.strftime("%Y%m%d%H%M%S"))
        Date = str(datetime.date.today())
        Time = str(now.time())
        Payment = '현금'
        DateTime = str(datetime.datetime.now())

        if cashReceived == '':
            pass
        elif orderMain.totalPrice > int(cashReceived):
            currentCash += int(cashReceived)
            sql1 = "INSERT INTO Sale (NoSale, Date, Time, Price, Payment) VALUES (%s, '%s', '%s', %s, '%s')" %\
                   (NoSale, Date, Time, int(cashReceived), Payment)
            sql3 = "INSERT INTO MANAGEMENT (DateTime, Total) VALUES ('%s', %s)" % (DateTime, currentCash)
            try:
                conn = sqlite3.connect("pos.db")
                c = conn.cursor()
                c.execute(sql1)
                c.execute(sql3)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setText("문제가 발생하여 결제가 완료되지 않았습니다\n재시도 하십시오")
                warning.setWindowTitle("오류")
                warning.exec()
            orderMain.totalPrice = orderMain.totalPrice - int(cashReceived)
            cashReceived = ''
            self.priceBox.setPlainText('{:,}'.format(orderMain.totalPrice))
            self.cashBox.setPlainText(cashReceived)
        else:
            change = int(cashReceived) - orderMain.totalPrice
            cashReceived = ''
            currentCash = currentCash + orderMain.totalPrice - change
            self.changeBox.setPlainText('{:,}'.format(change))
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.question(self, '결제 완료', '결제가 완료되었습니다', QtWidgets.QMessageBox.Ok)

            sql1 = "INSERT INTO Sale (NoSale, Date, Time, Price, Payment) VALUES (%s, '%s', '%s', %s, '%s')"%\
                   (NoSale, Date, Time, orderMain.totalPrice, Payment)
            sql3 = "INSERT INTO MANAGEMENT (DateTime, Total) VALUES ('%s', %s)"%(DateTime, currentCash)
            try:
                conn = sqlite3.connect("pos.db")
                c = conn.cursor()
                c.execute(sql1)
                for i in orderMain.orderedItems:
                    sql2 = "INSERT INTO DetailedSale (NoSale, Product, No, Price) VALUES (%s, '%s', %s, %s)" %\
                           (NoSale, i, int(orderMain.orderModel.index(int(orderMain.orderedItems.index(i)), 2).data()),\
                            int(orderMain.orderModel.index(int(orderMain.orderedItems.index(i)), 3).data().replace(',','')))
                    c.execute(sql2)
                c.execute(sql3)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setText("문제가 발생하여 결제가 완료되지 않았습니다\n재시도 하십시오")
                warning.setWindowTitle("오류")
                warning.exec()
            self.close()
            orderMain.orderNo = 1
            orderMain.orderedItems = []
            orderMain.totalPrice = 0
            orderMain.orderModel = QtGui.QStandardItemModel()
            orderMain.orderModel.setHorizontalHeaderLabels(['No', '상품명', '수량', '금액'])
            self.order = user.Order(self)

    @pyqtSlot()
    def onGoBackBtnClicked(self):
        self.close()
        choosePayment.ChoosePayment(self)

