import datetime
import sys
import sqlite3
import pandas as pd
import pyqtgraph as pg
from PyQt5.QtCore import QModelIndex, pyqtSlot, QObject
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
#from PyQt5.uic.properties import QtGui

import user
from ui import accessAdmin
from ui import addProduct
from ui import cashAvailable
from ui import changePrice
from ui import chooseProductManagement
from ui import dateStat
from ui import deleteProduct
from ui import productStat
from ui import accessAdmin
from ui import orderMain

import time

class AdminAuth(accessAdmin.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.Form.show()
        self.initUI()

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def initUI(self):
        # connect button to function
        self.isPassword.clicked.connect(self.checkPassword)

    def checkPassword(self):
        if self.passwordInput.text() == '1234':
            self.openSaleStat()
        elif self.passwordInput.text() == '':
            self.showMessageBox('오류', '비밀번호를 입력하세요')
        else:
            self.showMessageBox('오류', '비밀번호가 틀립니다')

    # make new window of SaleStat
    def openSaleStat(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = SaleStat()



class SaleStat(dateStat.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QMainWindow()
        self.setupUi(self.Form)
        self.initUi()
        self.Form.show()

        # statflag -> how to show statistic data
        # whichflag -> sort by which(period or product)
        self.statflag = 0
        self.whichflag = 'date'

    def openCashAvailable(self):
        self.ca = AdminCash()
    def openProductManagement(self):
        self.pm = ProductManagement()
    def goBack(self):
        self.Form.close()
        self.us = orderMain.OrderMain()

    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour + ":" + min + ":" + sec)
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def initUi(self):
        self.updateTime()
        # self.timer = QtCore.QTimer(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        # connect buttons to functions
        self.graphBtn.clicked.connect(self.showStatAsGraph)  # 그래프
        self.tableBtn.clicked.connect(self.showStatAsTable)  # 표
        self.searchBtn.clicked.connect(self.showStatAsDefault)  # 조회
        self.goBackBtn.clicked.connect(self.goBack)
        self.productStatBtn.clicked.connect(self.sortByWich)
        self.cashAvailableBtn.clicked.connect(self.openCashAvailable)
        self.productManagementBtn.clicked.connect(self.openProductManagement)
        self.changeWidgetAttr(self.Form, 'table')

    # get database from 'Sale'table or 'DetailedSale'table
    def getDB(self, which):
        try:
            self.con = sqlite3.connect('pos.db')
            self.cur = self.con.cursor()

            # test input
            self.cur.execute("INSERT INTO Sale Values ('1','2005-11-12','12:00:00', '30000', 'cash');")
            # self.cur.execute("INSERT INTO Sale Values ('2','2014-12-31','12:00:00', '3', 'free');")
            # self.cur.execute("INSERT INTO Sale Values ('3','2018-11-01','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('4','2018-11-02','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('5','2018-11-03','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('6','2018-11-04','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('7','2018-11-05','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('8','2018-11-06','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('9','2018-12-07','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('10','2018-12-08','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('11','2018-12-09','12:00:00', '300', 'card');")
            # self.cur.execute("INSERT INTO Sale Values ('12','2017-12-10','12:00:00', '300', 'card');")
            #
            # self.cur.execute("INSERT INTO DetailedSale Values ('1','1','friedChicken','2','20000');")
            # self.cur.execute("INSERT INTO DetailedSale Values ('2','1','Beer','4','12000');")
            # self.cur.execute("INSERT INTO DetailedSale Values ('3','1','Coke','2','2000');")

            if which == 'date':
                self.sd, self.ed = self.getStatDate()
                if self.sd:
                    sql = """SELECT * FROM Sale WHERE Date BETWEEN '{0}' AND '{1}'""".format(self.sd, self.ed)
                else:
                    return 0
            elif which == 'product':
                sql = """SELECT * FROM DetailedSale"""

            self.cur.execute(sql)
            self.rows = self.cur.fetchall()
            if len(self.rows) == 0:
                return 0
            else:
                return self.rows
        except sqlite3.Error as e:
            print(e)
        finally:
            self.con.close()

    # make dataframe from database by specific criteria
    def changeDBtoDF(self, raw):
        if raw:
            if self.whichflag == 'date':
                return pd.DataFrame(raw, columns=['NoSale', 'date', 'time', 'price', 'payment'])
            elif self.whichflag == 'product':
                return pd.DataFrame(raw, columns=['ID', 'NoSale', 'Product', 'No', 'Price'])
        else:
            return 0

    # show data as a form of table
    def showStatAsTable(self):
        self.statflag = 0
        self.showStatSummary()
        self.changeWidgetAttr(self.Form, 'table')

        self.df = self.changeDBtoDF(self.getDB(self.whichflag))

        # if there is no data in database, do nothing
        if type(self.df) == int:
            return
        # else, show data by specific criteria(period or product)
        elif self.whichflag == 'date':
            self.viewBox.setRowCount((len(self.df)))
            self.viewBox.setColumnCount(len(self.df.iloc[0]))

            for row in range(len(self.df)):
                for cell in range(len(self.df.iloc[row])):
                    self.viewBox.setItem(row, cell, QTableWidgetItem(str(self.df.iloc[row][cell])))

            self.viewBox.setHorizontalHeaderLabels(self.df.columns)
            self.viewBox.resizeColumnsToContents()
        elif self.whichflag == 'product':
            self.productSum = self.df[['No', 'Price']].groupby([self.df['Product']])
            self.productDf = self.productSum.sum()
            self.productDf.reset_index(level=0, inplace=True)

            self.viewBox.setRowCount((len(self.productDf)))
            self.viewBox.setColumnCount(len(self.productDf.iloc[0]))

            for row in range(len(self.productDf)):
                for cell in range(len(self.productDf.iloc[row])):
                    self.viewBox.setItem(row, cell, QTableWidgetItem(str(self.productDf.iloc[row][cell])))

            self.viewBox.setHorizontalHeaderLabels(self.productDf.columns)
            self.viewBox.resizeColumnsToContents()

    # show data as a form of graph
    def showStatAsGraph(self):
        self.statflag = 1
        self.showStatSummary()
        self.changeWidgetAttr(self.Form, 'graph')
        self.df = self.changeDBtoDF(self.getDB(self.whichflag))

        # if there is no data in database, do nothing
        if type(self.df) == int:
            return
        # else, show data by specific criteria(period or product)
        elif self.whichflag == 'date':
            self.stat = pd.DataFrame()
            self.stat['year'] = self.df['date'].apply(lambda x: pd.to_datetime(str(x)).year)
            self.stat['month'] = self.df['date'].apply(lambda x: pd.to_datetime(str(x)).month)
            self.stat['price'] = self.df['price']

            self.monthSum = self.stat['price'].groupby([self.stat['year'], self.stat['month']])

            # xlist -> x axis, datetime
            # ylist -> y axis, sum of sales(~=price)
            self.xlist = []
            print(list(self.monthSum.groups.keys()))

            for i in list(self.monthSum.groups.keys()):
                self.xlist.append(str(i))
            self.ylist = self.monthSum.sum().tolist()

            self.redrawPlotWidget(self.xlist, self.ylist, self.whichflag)

        elif self.whichflag == 'product':
            self.productSum = self.df[['No', 'Price']].groupby([self.df['Product']])
            self.productDf = self.productSum.sum()
            self.productDf.reset_index(level=0, inplace=True)

            # xlist -> x axis, products
            # ylist -> y axis, sum of sales
            self.xlist = self.productDf['Product'].tolist()
            self.ylist = self.productDf['Price'].tolist()

            self.redrawPlotWidget(self.xlist, self.ylist, self.whichflag)

    def showStatAsDefault(self):
        # check if there is data or not
        self.exists = self.showStatSummary()
        if self.exists == 0:
            return
        # if data exists, then show data by default criteria
        else:
            if self.statflag == 0:
                self.showStatAsTable()
            else:
                self.showStatAsGraph()

    def showStatSummary(self):
        self.df = self.changeDBtoDF(self.getDB(self.whichflag))

        if type(self.df) == int:
            self.showMessageBox("warning", "기록이 존재하지 않습니다.")
            return 0
        elif self.whichflag == 'date':
            self.salesTotalBox.setText(str(self.df['price'].sum()))
            self.salesAvgBox.setText(str(round(self.df['price'].mean(), 2)))
            return 1

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "close", "are you sure to quit?", \
                                   QMessageBox.YES | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    # return dates of startdate and enddate where you wanna query data
    def getStatDate(self):
        self.startdate = self.startDate.date()
        self.enddate = self.endDate.date()

        if self.startdate < self.enddate:
            return self.startdate.toString(QtCore.Qt.ISODate), \
                   self.enddate.toString(QtCore.Qt.ISODate)
        else:
            self.showMessageBox('warning', '잘못된 기간 설정입니다.')
            return 0, 0

    def setStatDate(self):
        pass

    # switch the whichflag
    def sortByWich(self):
        if self.whichflag == 'date':
            self.whichflag = 'product'
            self.productStatBtn.setText("기간 별 통계 보기")
        elif self.whichflag == 'product':
            self.whichflag = 'date'
            self.productStatBtn.setText("품목 별 통계 보기")

class AdminCash(cashAvailable.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.initUI()
        self.Form.show()

    def initUI(self):
        self.searchBtn.clicked.connect(self.showCashAvailable)
        self.cashAvailableBtn.clicked.connect(self.resetCashAvailable)
        self.goBackBtn.clicked.connect(self.Form.close)
        self.updateTime()

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def showCashAvailable(self):
        try:
            #기존 DB상태
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            sql = "SELECT * FROM Management WHERE ID=1"
            c.execute(sql)
            data = c.fetchone()
            self.dbTotal = str(data[2])
            self.beforeBox.setText(self.dbTotal)
            conn.close()

            #입력한 상태
            self.cash_50000 = int(self.moneyBox50000.text()) * 50000
            self.cash_10000 = int(self.moneyBox10000.text()) * 10000
            self.cash_5000 = int(self.moneyBox5000.text()) * 5000
            self.cash_1000 = int(self.moneyBox1000.text()) * 1000
            self.cash_500 = int(self.moneyBox500.text()) * 500
            self.cash_100 = int(self.moneyBox100.text()) * 100
            self.cash_50 = int(self.moneyBox50.text()) * 50
            self.cash_10 = int(self.moneyBox10.text()) * 10
            self.cur_cash = self.cash_50000 + self.cash_10000 + self.cash_5000 + self.cash_1000 + self.cash_500 + self.cash_100 + self.cash_50 + self.cash_10
            self.afterBox.setText(str(self.cur_cash))

            #차액 결제
            self.remain = int(self.dbTotal)-int(self.cur_cash)
            self.errorBox.setText(str(self.remain))

        except sqlite3.Error as e:
            print(e)

    def resetCashAvailable(self):
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            dateTime = datetime.datetime.now()
            sql = "UPDATE Management SET Total='%d' WHERE ID=1" %self.cur_cash
            c.execute(sql)
            sql = "UPDATE Management SET DateTime='%s' WHERE ID=1" % dateTime
            c.execute(sql)
            conn.commit()
            conn.close()
            self.beforeBox.clear()
            self.afterBox.clear()
            self.errorBox.clear()

        except sqlite3.Error as e:
            print(e)
            self.showMessageBox('오류',"문제가 발생하여 변경이 완료되지 않았습니다\n재시도 하십시오")
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("문제가 발생하여 변경이 완료되지 않았습니다\n재시도 하십시오")
            #warning.setWindowTitle("오류")
            #warning.exec()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour + ":" + min + ":" + sec)


class ProductManagement(chooseProductManagement.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.initUi()
        self.Form.show()

    def initUi(self):
        self.addProductBtn.clicked.connect(self.openAddProduct)
        self.deleteProductBtn.clicked.connect(self.openDeleteProduct)
        self.changePriceBtn.clicked.connect(self.openChangePrice)
        self.goBackBtn.clicked.connect(self.Form.close)

    def openAddProduct(self):
        self.addProdcutWindow = addProduct.AddProduct()

    def openDeleteProduct(self):
        self.deleteProdcutWindow = deleteProduct.DeleteProduct()

    def openChangePrice(self):
        self.changePriceWindow = changePrice.ChangePrice()