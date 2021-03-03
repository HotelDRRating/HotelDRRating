import pymysql as psql

__dbname = "hotelDRRating"
__tblname = "rsakeys"
def create_db():
    conn=psql.connect(host='localhost',user='root',password='')
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {__dbname}")
    finally:
        conn.close()
def create_table():
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {__tblname}(_id INTEGER AUTO_INCREMENT PRIMARY KEY, _privateKey VARCHAR(2000) NOT NULL, _publicKey VARCHAR(2000) NOT NULL,_email TEXT NOT NULL)")
            conn.commit()
    finally:
        conn.close()
def insert(privatekey,publickey,email):
    conn= psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO `rsakeys`(_privateKey,_publickey_email) VALUES(`{privatekey}`,`{publickey}`,`{email}`);")
            conn.commit()
    finally:
        conn.close()
def getKeys(email):
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM `rsakeys` WHERE _email = `{email}`")
            row = cursor.fetchone()
            return {"privatekey": row[1], "publickey" : row[2]}
    finally:
        conn.close()