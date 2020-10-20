# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refund.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from sqlite3 import *


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.resultListBox = QtWidgets.QTextEdit(Form)
        self.resultListBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.resultListBox.setGeometry(QtCore.QRect(12, 338, 1471, 551))
        self.resultListBox.setObjectName("resultListBox")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(8, 10, 1418, 318))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.timeLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.timeLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QTextEdit(self.widget)
        self.timeBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeBox.setReadOnly(True)
        self.timeBox.setMinimumSize(QtCore.QSize(400, 100))
        self.timeBox.setMaximumSize(QtCore.QSize(400, 100))
        self.timeBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout_2.addWidget(self.timeBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.goBackBtn = QtWidgets.QPushButton(self.widget)
        self.goBackBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.goBackBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.goBackBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.managementBtn = QtWidgets.QPushButton(self.widget)
        self.managementBtn.setEnabled(False)
        self.managementBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.managementBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.managementBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.managementBtn.setObjectName("managementBtn")
        self.horizontalLayout.addWidget(self.managementBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PayNoBox = QtWidgets.QLineEdit(self.widget)
        self.onlyNum = QDoubleValidator()
        self.PayNoBox.setValidator(self.onlyNum)
        self.PayNoBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.PayNoBox.setMinimumSize(QtCore.QSize(500, 100))
        self.PayNoBox.setMaximumSize(QtCore.QSize(500, 100))
        self.PayNoBox.setObjectName("PayNoBox")
        self.horizontalLayout_3.addWidget(self.PayNoBox)
        self.searchByPayNoBtn = QtWidgets.QPushButton(self.widget)
        self.searchByPayNoBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.searchByPayNoBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.searchByPayNoBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.searchByPayNoBtn.setObjectName("searchByPayNoBtn")
        self.horizontalLayout_3.addWidget(self.searchByPayNoBtn)
        self.refundBtn = QtWidgets.QPushButton(self.widget)
        self.refundBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.refundBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.refundBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.refundBtn.setObjectName("refundBtn")
        self.refundBtn.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.refundBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cardNoBox = QtWidgets.QLineEdit(self.widget)
        self.cardNoBox.setDisabled(True)
        self.cardNoBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.cardNoBox.setMinimumSize(QtCore.QSize(500, 100))
        self.cardNoBox.setMaximumSize(QtCore.QSize(500, 100))
        self.cardNoBox.setObjectName("cardNoBox")
        self.horizontalLayout_4.addWidget(self.cardNoBox)
        self.searchByCardNoBtn = QtWidgets.QPushButton(self.widget)
        self.searchByCardNoBtn.setDisabled(True)
        self.searchByCardNoBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.searchByCardNoBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.searchByCardNoBtn.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.searchByCardNoBtn.setObjectName("searchByCardNoBtn")
        self.horizontalLayout_4.addWidget(self.searchByCardNoBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel.setText(_translate("Form", "현재 시각: "))
        self.goBackBtn.setText(_translate("Form", "돌아가기"))
        self.managementBtn.setText(_translate("Form", "관리"))
        self.searchByPayNoBtn.setText(_translate("Form", "결제 번호로 조회"))
        self.refundBtn.setText(_translate("Form", "환불"))
        self.searchByCardNoBtn.setText(_translate("Form", "카드 번호로 조회"))


class Refund(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.searchByPayNoBtn.clicked.connect(self.searchByPayNo)
        self.refundBtn.clicked.connect(self.refund)
        self.goBackBtn.clicked.connect(self.goBackToMain)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.show()

    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min  = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour+":"+min+":"+sec)

    @pyqtSlot()
    def searchByPayNo(self):
        self.resultListBox.clear()
        flag = self.checkValidation(self.PayNoBox.text())
        if flag==False:
            return
        self.refundBtn.setEnabled(True)
        pay_no = int(self.PayNoBox.text())
        sql = "SELECT * FROM Sale WHERE NoSale='%d'" %pay_no
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            data = c.fetchall()
            conn.close()
            for i in data:
                self.resultListBox.append(str(i))
                return data
        except Error as e:
            print(e)

    def checkValidation(self, no):
        if no == '':
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("결제 번호를 기재하십시오.")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        no = int(no)
        sql = "SELECT * FROM Sale WHERE NoSale='%d'" % no
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            data = c.fetchall()
            conn.close()
            if data == []:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setText("결제 내역이 없습니다.")
                warning.setWindowTitle("오류")
                warning.exec()
                return False
            else:
                return data
        except Error as e:
            print(e)

    def searchByCardNo(self):
        pass

    def refund(self):
        data = self.checkValidation(self.PayNoBox.text())
        if data==False:
            return

        # 현금이면 시재관리
        data = list(data)
        if data[0][4] == '현금':
            self.cashAvailable(data[0][3])
        pay_no = int(self.PayNoBox.text())
        sql = "DELETE FROM Sale WHERE NoSale='%d'" % pay_no
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
        except Error as e:
            print(e)
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("문제가 발생하여 환불이 완료되지 않았습니다\n재시도 하십시오")
            warning.setWindowTitle("오류")
            warning.exec()
        self.PayNoBox.clear()
        self.resultListBox.clear()
        self.refundBtn.setEnabled(False)

    def cashAvailable(self, cost):
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            sql = "SELECT * FROM Management WHERE ID=1"
            c.execute(sql)
            data = c.fetchone()
            total = int(data[2]) + cost
            dateTime = datetime.datetime.now()
            sql = "UPDATE Management SET Total='%d' WHERE ID=1" %total
            c.execute(sql)
            sql = "UPDATE Management SET DateTime='%s' WHERE ID=1" % dateTime
            c.execute(sql)
            conn.commit()
            conn.close()
        except Error as e:
            print(e)

    def goBackToMain(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    e = Refund()
    sys.exit(app.exec_())

