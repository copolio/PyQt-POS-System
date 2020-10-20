# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addProduct.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(12, 8, 1518, 122))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setMinimumSize(QtCore.QSize(250, 80))
        self.timeLabel.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QTextBrowser(self.widget)
        self.timeBox.setMinimumSize(QtCore.QSize(250, 80))
        self.timeBox.setMaximumSize(QtCore.QSize(250, 80))
        self.timeBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.timeBox.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.horizontalLayout.addWidget(self.timeBox)
        self.deleteProductBtn = QtWidgets.QPushButton(self.widget)
        self.deleteProductBtn.setEnabled(False)
        self.deleteProductBtn.setMinimumSize(QtCore.QSize(300, 120))
        self.deleteProductBtn.setMaximumSize(QtCore.QSize(300, 120))
        self.deleteProductBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.deleteProductBtn.setObjectName("deleteProductBtn")
        self.horizontalLayout.addWidget(self.deleteProductBtn)
        self.changePriceBtn = QtWidgets.QPushButton(self.widget)
        self.changePriceBtn.setEnabled(False)
        self.changePriceBtn.setMinimumSize(QtCore.QSize(300, 120))
        self.changePriceBtn.setMaximumSize(QtCore.QSize(300, 120))
        self.changePriceBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.changePriceBtn.setObjectName("changePriceBtn")
        self.horizontalLayout.addWidget(self.changePriceBtn)
        self.goBackBtn = QtWidgets.QPushButton(self.widget)
        self.goBackBtn.setMinimumSize(QtCore.QSize(300, 120))
        self.goBackBtn.setMaximumSize(QtCore.QSize(300, 120))
        self.goBackBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 150, 1554, 122))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chickenBtn = QtWidgets.QPushButton(self.widget1)
        self.chickenBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.chickenBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.chickenBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(252, 190, 113);")
        self.chickenBtn.setObjectName("chickenBtn")
        self.horizontalLayout_2.addWidget(self.chickenBtn)
        self.beverageBtn = QtWidgets.QPushButton(self.widget1)
        self.beverageBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.beverageBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.beverageBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(85, 201, 234);")
        self.beverageBtn.setObjectName("beverageBtn")
        self.horizontalLayout_2.addWidget(self.beverageBtn)
        self.othersBtn = QtWidgets.QPushButton(self.widget1)
        self.othersBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.othersBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.othersBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(159, 217, 111);")
        self.othersBtn.setObjectName("othersBtn")
        self.horizontalLayout_2.addWidget(self.othersBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 280, 721, 571))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.showProductBox = QtWidgets.QListView(Form)
        self.showProductBox.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showProductBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.showProductBox.setGeometry(QtCore.QRect(20, 290, 700, 550))
        self.showProductBox.setMinimumSize(QtCore.QSize(700, 550))
        self.showProductBox.setMaximumSize(QtCore.QSize(700, 550))
        self.showProductBox.setObjectName("showProductBox")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(830, 281, 558, 422))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.productNameLabel = QtWidgets.QLabel(self.widget2)
        self.productNameLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.productNameLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.productNameLabel.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.productNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.productNameLabel.setObjectName("productNameLabel")
        self.horizontalLayout_4.addWidget(self.productNameLabel)
        self.productNameBox = QtWidgets.QLineEdit(self.widget2)
        self.productNameBox.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.productNameBox.setMinimumSize(QtCore.QSize(350, 100))
        self.productNameBox.setMaximumSize(QtCore.QSize(350, 100))
        self.productNameBox.setObjectName("productNameBox")
        self.horizontalLayout_4.addWidget(self.productNameBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.priceLabel = QtWidgets.QLabel(self.widget2)
        self.priceLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.priceLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.priceLabel.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.priceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLabel.setObjectName("priceBox")
        self.horizontalLayout_5.addWidget(self.priceLabel)
        self.priceBox = QtWidgets.QLineEdit(self.widget2)
        self.onlyNum = QIntValidator()
        self.priceBox.setValidator(self.onlyNum)
        self.priceBox.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.priceBox.setMinimumSize(QtCore.QSize(350, 100))
        self.priceBox.setMaximumSize(QtCore.QSize(350, 100))
        self.priceBox.setObjectName("priceLabel")
        self.horizontalLayout_5.addWidget(self.priceBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.categoryLabel = QtWidgets.QLabel(self.widget2)
        self.categoryLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.categoryLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.categoryLabel.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.categoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryLabel.setObjectName("categoryLabel")
        self.horizontalLayout_6.addWidget(self.categoryLabel)
        self.categoryBox = QtWidgets.QLineEdit(self.widget2)
        self.categoryBox.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.categoryBox.setMinimumSize(QtCore.QSize(350, 100))
        self.categoryBox.setMaximumSize(QtCore.QSize(350, 100))
        self.categoryBox.setObjectName("categoryBox")
        self.horizontalLayout_6.addWidget(self.categoryBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.addProductBtn = QtWidgets.QPushButton(self.widget2)
        self.addProductBtn.setMinimumSize(QtCore.QSize(200, 100))
        self.addProductBtn.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.addProductBtn.setFont(font)
        self.addProductBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(255, 94, 97);")
        self.addProductBtn.setObjectName("addProductBtn")
        self.horizontalLayout_3.addWidget(self.addProductBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel.setText(_translate("Form", "현재 시각: "))
        self.deleteProductBtn.setText(_translate("Form", "품목 삭제"))
        self.changePriceBtn.setText(_translate("Form", "가격 변경"))
        self.goBackBtn.setText(_translate("Form", "돌아가기"))
        self.chickenBtn.setText(_translate("Form", "치킨"))
        self.beverageBtn.setText(_translate("Form", "음료"))
        self.othersBtn.setText(_translate("Form", "기타"))
        self.productNameLabel.setText(_translate("Form", "제품명"))
        self.priceLabel.setText(_translate("Form", "금액"))
        self.categoryLabel.setText(_translate("Form", "카테고리"))
        self.addProductBtn.setText(_translate("Form", "추가"))

class AddProduct(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.chickenBtn.clicked.connect(self.sortByChicken)
        self.beverageBtn.clicked.connect(self.sortByDrink)
        self.othersBtn.clicked.connect(self.sortByOther)
        self.addProductBtn.clicked.connect(self.addProduct)
        self.deleteProductBtn.clicked.connect(self.gotoDeleteProduct)
        self.changePriceBtn.clicked.connect(self.gotoChangePrice)
        self.goBackBtn.clicked.connect(self.goBack)
        self.show()

    @pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min  = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour+":"+min+":"+sec)

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
            self.showProductBox.setModel(model)
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
            self.showProductBox.setModel(model)
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
            self.showProductBox.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @pyqtSlot()
    def addProduct(self):
        name = self.productNameBox.text()
        price = int(self.priceBox.text())
        category = self.categoryBox.text()
        flag = self.checkValidation(name, price, category)
        if flag==False:
            return
        sql = "INSERT INTO Product(Name, Price, Category) VALUES ('%s','%d','%s')" % (name, price, category)
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("문제가 발생하여 추가가 완료되지 않았습니다\n재시도 하십시오")
            warning.setWindowTitle("오류")
            warning.exec()
        self.productNameBox.clear()
        self.priceBox.clear()
        self.categoryBox.clear()
        self.sortByChicken()

    @pyqtSlot()
    def checkValidation(self, name, price, category):
        if name == '' or price == '' or category == '':
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("기재하지 않은 내용이 있습니다.")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        categoryList = ['치킨', '음료', '기타']
        if category not in categoryList:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("존재하지 않는 카테고리 입니다.")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        if price < 0:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("0이상의 금액을 입력해주십시오")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        sql = "SELECT * FROM Product WHERE Name='%s'" % name
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            nameCheck = c.fetchall()
            conn.close()
            if nameCheck != []:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setText("이미 존재하는 품목명입니다.")
                warning.setWindowTitle("오류")
                warning.exec()
                return False
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return False

    @pyqtSlot()
    def gotoDeleteProduct(self):
        pass

    @pyqtSlot()
    def gotoChangePrice(self):
        pass

    @pyqtSlot()
    def goBack(self):
        self.close()