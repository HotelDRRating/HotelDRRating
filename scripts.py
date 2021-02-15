import pymysql as psql
class MissingArgsValueException(Exception):
    def __init__(self,message="There is a NoneType object in the values passed"):
        super().__init__(self.message)
class hotelDB(object):
    __dbname = "hotelDRRating"
    def __init__(self):
        try:
            connection = psql.connect(host='localhost',user='root',password='')
            cursor = connection.cursor()
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.__dbname}')
            conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
            curs = conn.cursor()
            curs.execute("CREATE TABLE IF NOT EXISTS hotelInfo(_id INTEGER AUTO_INCREMENT PRIMARY KEY,_hotel TEXT NOT NULL,_fullname TEXT NOT NULL,_email TEXT NOT NULL,password TEXT NOT NULL)")
        finally:
            connection.close()
            conn.close()
        return
    def insert(self,hotel:str,fullname:str,email:str,password:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            with conn.cursor as cursor:
                cursor.execute(f"INSERT INTO hotelInfo(_id,_hotel,_fullname,_email,_password) VALUES(null,'{hotel}','{fullname}','{email}','{password}'")
            return True
        except:
            return False
        finally:
            conn.close()
    def test(self):
        raise MissingArgsValueException()
            
a = hotelDB()
