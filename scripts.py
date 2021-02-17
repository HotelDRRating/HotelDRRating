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
class crypto(object):
    __dbname = "hotelDRRating"
    def __init__(self,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            with conn.cursor() as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS `rsakeys` ( `_id` INT NOT NULL AUTO_INCREMENT , `_pubkey` VARCHAR(2000) NOT NULL , `_privkey` VARCHAR(2000) NOT NULL , `_email` TEXT NOT NULL , PRIMARY KEY (`id`))")
                conn.commit()
        finally:
            conn.close()
    def generate(self,user:str,keysize=2048,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        (self.pubkey, self.privkey) = rsa.newkeys(nbits=keysize)
        self.publickey = str(self.pubkey)
        self.privatekey = str(self.privkey)
        try:
            sql = f"INSERT INTO `rsakeys`(_pubkey,_privkey,_user) VALUES('{self.pubkey}','{self.privkey}','{user}')"
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
        finally:
            conn.close()
    def get_keys(self, email:str,conn=psql.connect(host='localhost',user='root',password='',database=__dbname)):
        try:
            sql = f"SELECT FROM rsakeys WHERE _email = '{email}'"
            with conn.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchone()
                return {"public" : row[1], "private" : row[2]}
        finally:
            conn.close()
    def encrypt(self,hotel:str,fullname:str,email:str,password:str):
        
        self.pubkey = self.get_keys(email=email)["public"]
        nhotel = hotel.encode('utf-8')
        nfullname = fullname.encode('utf-8')
        nemail = email.encode('utf-8')
        npassword = password.encode('utf-8')
        #return (rsa.encrypt(nemail,self.pubkey),rsa.encrypt(nhotel,self.pubkey),rsa.encrypt(nemail,self.pubkey),rsa.encrypt(npassword,self.pubkey))
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
        

