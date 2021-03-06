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
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {__tblname}(_id INTEGER AUTO_INCREMENT PRIMARY KEY, _privateKey VARCHAR(2000) NOT NULL, _publicKey VARCHAR(2000) NOT NULL,_hash TEXT NOT NULL)")
            conn.commit()
    finally:
        conn.close()
def insert(privatekey,publickey,hash):
    conn= psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO `rsakeys`(_privateKey,_publickey_hash) VALUES(`{privatekey}`,`{publickey}`,`{hash}`);")
            conn.commit()
    finally:
        conn.close()
def getKeys(hash):
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM `rsakeys` WHERE _hash = `{hash}`")
            row = cursor.fetchone()
            return {"private": row[1], "public" : row[2]}
    finally:
        conn.close()
def delete(hash):
    conn=psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"DELETE FROM hotelinfo WHERE _hash = '{hash}'")
            conn.commit()
            return True
    except:
        return False
    finally:
        conn.close()