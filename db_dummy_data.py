# POS 데이터베이스 클래스
# 프로그램 초기 실행시 DB 초기화 설정을 위한 코드

import sqlite3
from sqlite3 import Error

class DummyData:
    def createConnection(self):
        conn = None
        try:
            conn = sqlite3.connect("pos.db")
            return conn
        except Error as e:
            print(e)
        return conn

    def insert(self, conn, sql):
        try:
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
        except Error as e:
            print(e)

    def __init__(self):
        sql1 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191130022001,'2019-11-30','02:20:01',20000,'현금')"""
        sql2 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191130133030,'2019-11-30','13:30:30',32000,'카드')"""
        sql3 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191201144110,'2019-12-01','14:41:10',45000,'카드')"""
        sql4 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191201153000,'2019-12-01','15:30:00',24000,'현금')"""
        conn = self.createConnection()
        if conn is not None:
            self.insert(conn, sql1)
            self.insert(conn, sql2)
            self.insert(conn, sql3)
            self.insert(conn, sql4)
        else:
            print("Error. Cannot insert the data.")

DummyData()