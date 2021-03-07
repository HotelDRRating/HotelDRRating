import pymysql as psql
__dbname = "hotelDRRating"
__tblname = "hotelinfo"
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
            cursor.execute("CREATE TABLE IF NOT EXISTS {__tblname}(_id INTEGER AUTO_INCREMENT PRIMARY KEY,_hotel TEXT NOT NULL,_fullname TEXT NOT NULL,_email TEXT NOT NULL,_password TEXT NOT NULL,_hash TEXT NOT NULL,_verified INTEGER NOT NULL)")
            conn.commit()
            
    finally:
        conn.close()
def insert(hotel,fullname,email,password,hash):
    conn=psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO `{__tblname}`(_hotel,_fullname,_email,_password,_otp,_verified) VALUES('{hotel}','{fullname}','{email}','{password}',{hash},0);")
            conn.commit()
    finally:
        conn.close()
def verify(hash):
    conn=psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:        
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM {__tblname} WHERE _hash = '{hash}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row[5] == hash:
                sql = f"UPDATE `{__tblname}` SET(_verified = 1) WHERE _hash = '{hash}'"
                cursor.execute(sql)
                conn.commit()
    finally:
        conn.close()
def is_verified(hash):
    conn=psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:        
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM {__tblname} WHERE _hash = '{hash}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row[6] == 1
    finally:
        conn.close()
def get(hash):
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM {__tblname} WHERE _hash = '{hash}'"
            cursor.execute(sql)
            row = cursor.fetchone()

            return {'hotel':row[1],'fullname':row[2],'email':row[3],'password':row[4],'hash':row[5]}
    finally:
        conn.close()
def delete(hash):
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {__tblname} WHERE _hash = '{hash}'"
            cursor.execute(sql)
            conn.commit()
    finally:
        conn.close()