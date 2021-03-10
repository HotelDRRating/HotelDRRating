import pymysql as psql
__dbname = "hotelDRRating"
def create_table():
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS rsakeys(_id INTEGER AUTO_INCREMENT PRIMARY KEY, _privateKey TEXT NOT NULL, _publicKey TEXT NOT NULL,_hash TEXT NOT NULL)")
            conn.commit()
    finally:
        conn.close()
def insert(privatekey,publickey,hash):
    conn= psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO rsakeys(_privateKey,_publickey,_hash) VALUES('{privatekey}','{publickey}','{hash}')"
            cursor.execute(sql)
            conn.commit()
    finally:
        conn.close()
def getKeys(hash):
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM rsakeys WHERE _hash = '{hash}'")
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
create_table()