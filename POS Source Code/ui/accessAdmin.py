# 관리자 인증
from PyQt5 import QtCore, QtGui, QtWidgets

# QtDesigner를 통해 생성한 UI 폼
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.chickenLabel = QtWidgets.QLabel(self.splitter)
        self.chickenLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.chickenLabel.setStyleSheet("image: url(:/newPrefix/admin.png);")
        self.chickenLabel.setText("")
        self.chickenLabel.setObjectName("chickenLabel")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.passwordInput = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setMinimumSize(QtCore.QSize(30, 30))
        self.passwordInput.setMaximumSize(QtCore.QSize(500, 100))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.horizontalLayout.addWidget(self.passwordInput)
        self.isPassword = QtWidgets.QPushButton(self.layoutWidget)
        self.isPassword.setMinimumSize(QtCore.QSize(100, 100))
        self.isPassword.setMaximumSize(QtCore.QSize(100, 100))
        self.isPassword.setStyleSheet("image: url(:/newPrefix/login.png);\n"
"border: none;")
        self.isPassword.setText("")
        self.isPassword.setObjectName("isPassword")
        self.horizontalLayout.addWidget(self.isPassword)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import ui.source