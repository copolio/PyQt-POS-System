import sqlite3

def addProduct():
    for i in range(50000,100001):
        sql = "INSERT INTO Sale(NoSale, Date, Time, Price, Payment) VALUES ('%s','0','0','0','현금')" % i
        try:
            conn = sqlite3.connect("pos.db")
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        print("done",i)

addProduct()