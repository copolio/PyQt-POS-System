# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePrice.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


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
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 8, 1518, 122))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(120, 50))
        self.timeLabel.setMaximumSize(QtCore.QSize(120, 50))
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
        self.timeBox = QtWidgets.QTextBrowser(self.layoutWidget)
        self.timeBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeBox.setMinimumSize(QtCore.QSize(180, 50))
        self.timeBox.setMaximumSize(QtCore.QSize(180, 50))
        self.timeBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout.addWidget(self.timeBox)
        self.addProductBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.addProductBtn.setEnabled(False)
        self.addProductBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.addProductBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.addProductBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.addProductBtn.setObjectName("addProductBtn")
        self.horizontalLayout.addWidget(self.addProductBtn)
        self.deleteProductBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteProductBtn.setEnabled(False)
        self.deleteProductBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.deleteProductBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.deleteProductBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.deleteProductBtn.setObjectName("deleteProductBtn")
        self.horizontalLayout.addWidget(self.deleteProductBtn)
        self.goBackBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.goBackBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.goBackBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.goBackBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 150, 1554, 122))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chickenBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.chickenBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.chickenBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.chickenBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(252, 190, 113);")
        self.chickenBtn.setObjectName("chickenBtn")
        self.horizontalLayout_2.addWidget(self.chickenBtn)
        self.beverageBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.beverageBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.beverageBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.beverageBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(85, 201, 234);")
        self.beverageBtn.setObjectName("beverageBtn")
        self.horizontalLayout_2.addWidget(self.beverageBtn)
        self.othersBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.othersBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.othersBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.othersBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(159, 217, 111);")
        self.othersBtn.setObjectName("othersBtn")
        self.horizontalLayout_2.addWidget(self.othersBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.othersBtn.raise_()
        self.chickenBtn.raise_()
        self.beverageBtn.raise_()
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
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(830, 281, 558, 422))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.productNameLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.productNameLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.productNameLabel.setMaximumSize(QtCore.QSize(200, 50))
        self.productNameLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\"")
        self.productNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.productNameLabel.setObjectName("productNameLabel")
        self.horizontalLayout_4.addWidget(self.productNameLabel)
        self.productNameBox = QtWidgets.QLineEdit(self.layoutWidget2)
        self.productNameBox.setStyleSheet("font: 75 20pt \"함초롬돋움\"")
        self.productNameBox.setMinimumSize(QtCore.QSize(400, 100))
        self.productNameBox.setMaximumSize(QtCore.QSize(400, 100))
        self.productNameBox.setObjectName("productNameBox")
        self.horizontalLayout_4.addWidget(self.productNameBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.originalPriceLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.originalPriceLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.originalPriceLabel.setMaximumSize(QtCore.QSize(200, 50))
        self.originalPriceLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.originalPriceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originalPriceLabel.setObjectName("originalPriceLabel")
        self.horizontalLayout_5.addWidget(self.originalPriceLabel)
        self.originalPriceBox = QtWidgets.QLineEdit(self.layoutWidget2)
        self.onlyNum = QIntValidator()
        self.originalPriceBox.setValidator(self.onlyNum)
        self.originalPriceBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";\n")
        self.originalPriceBox.setMinimumSize(QtCore.QSize(400, 100))
        self.originalPriceBox.setMaximumSize(QtCore.QSize(400, 100))
        self.originalPriceBox.setObjectName("originalPriceBox")
        self.horizontalLayout_5.addWidget(self.originalPriceBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.newPriceLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.newPriceLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.newPriceLabel.setMaximumSize(QtCore.QSize(200, 50))
        self.newPriceLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.newPriceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newPriceLabel.setObjectName("newPriceLabel")
        self.horizontalLayout_6.addWidget(self.newPriceLabel)
        self.newPriceBox = QtWidgets.QLineEdit(self.layoutWidget2)
        self.newPriceBox.setValidator(self.onlyNum)
        self.newPriceBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";\n")
        self.newPriceBox.setMinimumSize(QtCore.QSize(400, 100))
        self.newPriceBox.setMaximumSize(QtCore.QSize(400, 100))
        self.newPriceBox.setObjectName("newPriceBox")
        self.horizontalLayout_6.addWidget(self.newPriceBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.changePriceBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.changePriceBtn.setMinimumSize(QtCore.QSize(200, 100))
        self.changePriceBtn.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.changePriceBtn.setFont(font)
        self.changePriceBtn.setStyleSheet("font: 75 25pt \"함초롬돋움\";\n"
"background-color: rgb(255, 94, 97);")
        self.changePriceBtn.setObjectName("changePriceBtn")
        self.horizontalLayout_3.addWidget(self.changePriceBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel.setText(_translate("Form", "현재 시각: "))
        self.addProductBtn.setText(_translate("Form", "품목 추가"))
        self.deleteProductBtn.setText(_translate("Form", "품목 삭제"))
        self.goBackBtn.setText(_translate("Form", "돌아가기"))
        self.chickenBtn.setText(_translate("Form", "치킨"))
        self.beverageBtn.setText(_translate("Form", "음료"))
        self.othersBtn.setText(_translate("Form", "기타"))
        self.productNameLabel.setText(_translate("Form", "제품명"))
        self.originalPriceLabel.setText(_translate("Form", "기존 금액"))
        self.newPriceLabel.setText(_translate("Form", "변경 금액"))
        self.changePriceBtn.setText(_translate("Form", "변경"))

class ChangePrice(QMainWindow, Ui_Form):
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
        self.showProductBox.clicked.connect(self.passProductName)
        self.changePriceBtn.clicked.connect(self.changePrice)

        self.addProductBtn.clicked.connect(self.gotoAddProduct)
        self.deleteProductBtn.clicked.connect(self.gotoDeleteProduct)
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

    @pyqtSlot(QModelIndex)
    def passProductName(self, index):
        self.productNameBox.setText(index.data())
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            sql = "SELECT * FROM Product WHERE Name='%s'" % index.data()
            c.execute(sql)
            data = c.fetchone()
            price = str(data[2])
            self.originalPriceBox.setText(price)
            conn.close()
        except sqlite3.Error as e:
            print(e)

    @pyqtSlot()
    def checkValidation(self, productName, productPrice, newPrice):
        if productName == '' or productPrice == '' or newPrice == '':
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("기재하지 않은 내용이 있습니다.")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        if productPrice < 0 or newPrice < 0:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("0이상의 금액을 입력하십시오")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        sql = "SELECT * FROM Product WHERE Name='%s'" % productName
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            nameCheck = c.fetchall()
            conn.close()
            if nameCheck == []:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setText("존재하지 않는 품목명입니다.")
                warning.setWindowTitle("오류")
                warning.exec()
                return False
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return False

    @pyqtSlot()
    def changePrice(self):
        productName = self.productNameBox.text()
        productPrice = int(self.originalPriceBox.text())
        newPrice = int(self.newPriceBox.text())
        flag = self.checkValidation(productName, productPrice, newPrice)
        if flag==False:
            return
        sql = "UPDATE Product SET Price='%d' WHERE Name='%s'" % (newPrice, productName)
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
            warning.setText("문제가 발생하여 변경이 완료되지 않았습니다\n재시도 하십시오")
            warning.setWindowTitle("오류")
            warning.exec()

        self.productNameBox.clear()
        self.originalPriceBox.clear()
        self.newPriceBox.clear()
        self.sortByChicken()

    @pyqtSlot()
    def gotoAddProduct(self):
        pass

    @pyqtSlot()
    def gotoDeleteProduct(self):
        pass

    @pyqtSlot()
    def goBack(self):
        self.close()