import pymysql as psql,smtplib,ssl,rsa
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class hotelDB(object):
    __dbname = "hotelDRRating"
    def __init__(self):
        try:
            connection = psql.connect(host='localhost',user='root',password='')
            cursor = connection.cursor()
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.__dbname}')
            conn = psql.connect(host='localhost',user='root',password='',database=self.__dbname)
            curs = conn.cursor()
            curs.execute("CREATE TABLE IF NOT EXISTS hotelinfo(_id INTEGER AUTO_INCREMENT PRIMARY KEY,_hotel TEXT NOT NULL,_fullname TEXT NOT NULL,_email TEXT NOT NULL,_password TEXT NOT NULL)")
        finally:
            connection.close()
            conn.close()
        return
    def insert(self,hotel:str,fullname:str,email:str,password:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
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
       
    def update(self,where:str,hotel:str,fullname:str,email:str,password:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            with conn.cursor() as cursor:
                sql = f"UPDATE hotelinfo SET(_hotel='{hotel}',_fullname='{fullname},_email='{email}',_password='{password}')"
                cursor.execute(sql)
                conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()
    def getRecord(self, email:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM hotelinfo WHERE _email = '{email}'")
            return cursor.fetchone()
        finally:
            conn.close()
    def login_auth(self,email:str,password:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM hotelinfo WHERE _email = '{email}' AND _password = '{password}' ")
                row = cursor.fetchone()
                return email == row[3] and password == row[4]
        finally:
            conn.close()
    def delete(self, email:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM hotelinfo WHERE _email = '{email}'")
                conn.commit()
                return True
        except:
            return False
        finally:
            conn.close()
class binary(object):
    def __init__(self):
        return
    def convert_to_binary(self,hotel:str,fullname:str,email:str,password:str):
        self.hotel_binary = []
        self.fullname_binary = []
        self.email_binary = []
        self.password_binary = []
        for byte in hotel.encode('utf8'):
            self.hotel_binary.append(bin(byte))
        for byte in fullname.encode('utf8'):
            self.fullname_binary.append(bin(byte))
        for byte in email.encode('utf8'):
            self.email_binary.append(bin(byte))
        for byte in password.encode('utf8'):
            self.password_binary.append(bin(byte))
        
        return {"hotel":" ".join(self.hotel_binary),"fullname":" ".join(self.fullname_binary),"email":" ".join(self.email_binary),"password": " ".join(self.password_binary)}
    def convert_to_string(self,hotel:str,fullname:str,email:str,password:str):
        a = hotel.split(" ")
        b = fullname.split(" ")
        c = email.split(" ")
        d = password.split(" ") 
        return {"hotel":"".join([chr(int(q,2)) for q in a]), "fullname":"".join([chr(int(q, 2)) for q in b]), "email":"".join([chr(int(q,2)) for q in c]), "password":"".join([chr(int(q,2)) for q in d])}
class emailing(object):
    sender_email = 'V!6ga2$r6?Jf$8Ye¥oI1@73EG?o@kl7?yOp#¢5Bt$8YeB6$&a2$rr!0XV!6gp0t$Yo!fu$t!B6$&'#change and obfuscate later
    password = 'V!6gu$t!V!6g@73E8?Ty£tOyG?o@Pk&*q8u?'#change and obfuscate later
    def __init__(self):
        return
    def send_thank_you(self,email:str):
        if '@' not in email:
            raise ValueError
        s = []
        for q in list(email):
            if q == '@':
                break
            else:
                s.append(q)
        sender = "".join(s)
        message = MIMEMultipart('alternative')
        message["Subject"] = "Thank You"
        message["From"] = self.sender_email
        message["To"] = email
        msg = f"""\
            Thank you {sender} for reaching out to us our support team will get back to you within 24 hours

            Regards.
            The Disaster Resilience Rating For Hotels            
            """
        message.attach(MIMEText(msg,"plain"))

        with smtplib.SMTP_SSL('smtp.gmail.com',465, context = ssl.context()) as serv:
            serv.login(self.sender_email,self.password)
            serv.sendmail(self.sender_email,email,message.as_string())
            serv.close()
        

