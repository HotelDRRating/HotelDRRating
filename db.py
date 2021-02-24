import pymysql as psql

class Hotel(object):
    __dbname = "hotelDRRating"
    def __init__(self):
        self.create_db()
        self.create_hotelinfo_table()
    def create_db(self):
        conn=psql.connect(host='localhost',user='root',password='')
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__dbname}")
        finally:
            conn.close()
    def create_hotelinfo_table(self):
        conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:            
                cursor.execute("CREATE TABLE IF NOT EXISTS hotelinfo(_id INTEGER AUTO_INCREMENT PRIMARY KEY,_hotel TEXT NOT NULL,_fullname TEXT NOT NULL,_email TEXT NOT NULL,_password TEXT NOT NULL,_otp TEXT NOT NULL,_verified INTEGER NOT NULL)")
                conn.commit()
                return True
        except:
            return False
        finally:
            conn.close()
    def insert(self,hotel:str,fullname:str,email:str,password:str):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                sql = f"INSERT INTO `hotelinfo`(_hotel,_fullname,_email,_password) VALUES('{hotel}','{fullname}','{email}','{password}');"
                cursor.execute(sql)
                conn.commit()
                return True
        except:
            return False
        finally:
            conn.close()
    def is_verified(self,email):
        conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                sql = f"SELECT * FROM hotelinfo WHERE _email = '{email}'"
                cursor.execute(sql)
                row = cursor.fetchone()
                return row[6] == 1
        finally:
            conn.close()
    def verify(self,otp, email):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                sql = f"SELECT * FROM hotelinfo WHERE _email = '{email}'"
                cursor.execute(sql)
                row = cursor.fetchone()
                if row[5] == otp:
                    sql = f"UPDATE `hotelinfo` SET(_verified = 1) WHERE _email = '{email}'"
                    cursor.execute(sql)
                    conn.commit()
        finally:
            conn.close()
    def update(self,where:str,hotel:str,fullname:str,email:str,password:str):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                sql = f"UPDATE `hotelinfo` SET(_hotel='{hotel}',_fullname='{fullname},_email='{email}',_password='{password}') WHERE _email='{where}'"
                cursor.execute(sql)
                conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()
    def getRecord(self, email:str):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM hotelinfo WHERE _email = '{email}'")
            return cursor.fetchone()
        finally:
            conn.close()
    def login_auth(self,email:str,password:str):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM hotelinfo WHERE _email = '{email}' AND _password = '{password}' ")
                row = cursor.fetchone()
                return email == row[3] and password == row[4]
        finally:
            conn.close()
    def delete(self,email:str):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM hotelinfo WHERE _email = '{email}'")
                conn.commit()
                return True
        except:
            return False
        finally:
            conn.close()
class rsaDB(object):
    def __init__(self):
        self.create_db()
        self.create_rsakeys_table()
        return
    def create_db(self):
        conn=psql.connect(host='localhost',user='root',password='')
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__dbname}")
        finally:
            conn.close()
    def create_rsakeys_table(self):
        conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:            
                cursor.execute("CREATE TABLE IF NOT EXISTS rsakeys(_id INTEGER AUTO_INCREMENT PRIMARY KEY, _privateKey VARCHAR(2000) NOT NULL, _publicKey VARCHAR(2000) NOT NULL,_email TEXT NOT NULL")
                conn.commit()
                return True
        except:
            return False
        finally:
            conn.close()
    def insert(self,privatekey,publickey,email):
        conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO `rsakeys`(_privateKey,_publickey_email) VALUES(`{privatekey}`,`{publickey}`,`{email}`);")
                conn.commit()
        finally:
            conn.close()
    def getKeys(self,email):
        conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `rsakeys` WHERE _email = `{email}`")
                row = cursor.fetchone()
                return {"privatekey": row[1], "publickey" : row[2]}
        finally:
            conn.close()