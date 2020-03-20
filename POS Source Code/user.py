# 사용자
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui import initial
from ui import orderMain


# 사용자 인증
class UserAuth(initial.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.Form.show()
        self.initUI()

    def initUI(self):
        # connect button to function
        self.isPassword.clicked.connect(self.checkPassword)

    # 오류 발생시, 경고 알림 창 팝업
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
        else:
            self.showMessageBox('오류','비밀번호가 올바르지 않습니다')

    # 주문 화면 호출
    def openOrder(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = Order()


# 주문
class Order(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ds = orderMain.OrderMain()