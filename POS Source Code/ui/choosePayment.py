# 결제 방법 선택
from ui import cashPayment, orderMain
import user
from ui.orderMain import *

# QtDesigner를 통해 생성한 UI 폼
class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeLabel = QtWidgets.QLabel(Form)
        self.timeLabel.setMinimumSize(QtCore.QSize(300, 100))
        self.timeLabel.setMaximumSize(QtCore.QSize(170, 100))
        self.timeLabel.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QPlainTextEdit(Form)
        self.timeBox.setStyleSheet("font: 75 20pt \"함초롬돋움\";")
        self.timeBox.setReadOnly(True)
        self.timeBox.setMinimumSize(QtCore.QSize(300, 100))
        self.timeBox.setMaximumSize(QtCore.QSize(300, 100))
        self.timeBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout_2.addWidget(self.timeBox)
        spacerItem = QtWidgets.QSpacerItem(200, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.goBackBtn = QtWidgets.QPushButton(Form)
        self.goBackBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.goBackBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.goBackBtn.setFont(font)
        self.goBackBtn.setStyleSheet("font: 75 30pt \"함초롬돋움\";\n"
                                     "background-color: rgb(255, 129, 112);")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cashBtn = QtWidgets.QPushButton(Form)
        self.cashBtn.setMinimumSize(QtCore.QSize(400, 200))
        self.cashBtn.setMaximumSize(QtCore.QSize(150, 200))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.cashBtn.setFont(font)
        self.cashBtn.setStyleSheet("font: 75 45pt \"함초롬돋움\";\n"
                                   "background-color: rgb(0, 170, 127);")
        self.cashBtn.setObjectName("cashBtn")
        self.horizontalLayout_3.addWidget(self.cashBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.cardBtn = QtWidgets.QPushButton(Form)
        self.cardBtn.setMinimumSize(QtCore.QSize(400, 200))
        self.cardBtn.setMaximumSize(QtCore.QSize(150, 200))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.cardBtn.setFont(font)
        self.cardBtn.setStyleSheet("font: 75 45pt \"함초롬돋움\";\n"
                                   "background-color: rgb(170, 170, 127);")
        self.cardBtn.setObjectName("cardBtn")
        self.horizontalLayout_3.addWidget(self.cardBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel.setText(_translate("Form", "현재 시각: "))
        self.goBackBtn.setText(_translate("Form", "돌아가기"))
        self.cashBtn.setText(_translate("Form", "현금"))
        self.cardBtn.setText(_translate("Form", "카드"))


class ChoosePayment(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.cashBtn.clicked.connect(self.onCashBtnClicked)
        self.cardBtn.clicked.connect(self.onCardBtnClicked)
        self.goBackBtn.clicked.connect(self.onGoBackBtnClicked)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.show()

    # 현재 시각 출력 함수
    @pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour+":"+min+":"+sec)

    # 현금 결제 선택
    @pyqtSlot()
    def onCashBtnClicked(self):
        self.close()
        # 현금 결제 화면으로 전환
        cashPayment.CashPayment(self)

    # 카드 결제 선택
    @pyqtSlot()
    def onCardBtnClicked(self):
        msgbox = QtWidgets.QMessageBox(self)
        msgbox.question(self, 'POS Program Error', '지원되지 않는 기능입니다', QtWidgets.QMessageBox.Ok)

    @pyqtSlot()
    def onGoBackBtnClicked(self):
        self.close()
        self.order = user.Order(self)
