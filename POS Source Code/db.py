# 프로그램 초기 실행시 DB 초기 설정

import sqlite3
from sqlite3 import Error
import datetime

class POSDB:
    def createConnection(self):
        conn = None
        try:
            conn = sqlite3.connect("pos.db")
            return conn
        except Error as e:
            print(e)
        return conn

    def executeSql(self, conn, sql):
        try:
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
        except Error as e:
            print(e)

    def __init__(self):
        sqlCreateTable_Sale = """CREATE TABLE IF NOT EXISTS Sale (
                                    NoSale INTEGER PRIMARY KEY AUTOINCREMENT,
	                                Date date,
                                	Time time,
                                	Price integer,
                                	Payment varchar(255)
                                );"""
        sqlCreateTable_DetailedSale = """CREATE TABLE IF NOT EXISTS DetailedSale (
                                	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	                                NoSale integer FOREIGNKEY REFERENCES Sale(NoSale),
	                                Product varchar(255),
	                                No integer,
	                                Price integer
                                );"""
        sqlCreateTable_Management = """CREATE TABLE IF NOT EXISTS Management (
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    DateTime datetime NOT NULL,
                                    Total integer NOT NULL
                                );"""
        sqlCreateTable_Product = """CREATE TABLE IF NOT EXISTS Product (
                                    NoProduct INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Name varchar(255),
                                    Price integer,	
                                    Category varchar(255)
                                );"""
        currentTime = datetime.datetime.now()
        sqlInsertData_Management = "INSERT INTO Management(ID, DateTime, Total) VALUES (1,'%s',0)" % currentTime

        conn = self.createConnection()
        if conn is not None:
            self.executeSql(conn, sqlCreateTable_Sale)
            self.executeSql(conn, sqlCreateTable_DetailedSale)
            self.executeSql(conn, sqlCreateTable_Product)
            self.executeSql(conn, sqlCreateTable_Management)
            self.executeSql(conn, sqlInsertData_Management)
        else:
            print("Error. Cannot create the database connection.")
