import sys
import sqlite3
from PyQt5.QtCore import QModelIndex, pyqtSlot, QObject
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
#from PyQt5.uic.properties import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui import initial
from ui import orderMain
from ui import refund
from ui import cardPayment
from ui import cashPayment
from ui import choosePayment
import admin

class UserAuth(initial.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.Form.show()
        self.initUI()

    def initUI(self):
        # connect button to function
        self.isPassword.clicked.connect(self.checkPassword)
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def checkPassword(self):
        if self.passwordInput.text() == '1234':
            self.openOrder()
        elif self.passwordInput.text() == '':
            self.showMessageBox('오류','비밀번호를 입력하십시오')
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("비밀번호를 입력하십시오")
            #warning.setWindowTitle("오류")
            #warning.exec()
        else:
            self.showMessageBox('오류','비밀번호가 올바르지 않습니다')
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("비밀번호가 올바르지 않습니다")
            #warning.setWindowTitle("오류")
            #warning.exec()

    # make new window of SaleStat
    def openOrder(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = Order()

class Order(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ds = orderMain.OrderMain()