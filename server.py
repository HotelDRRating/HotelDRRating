from flask import Flask,redirect,url_for,render_template,request
import random,pymysql as psql
from CRYPT import c
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import base64 as b64
__NULL__ = ""
app = Flask(__name__)
def generate(bits=2048):
    return bits
def encrypt(msg,publickey):
    return 
@app.route('/',methods=["GET","POST"])
def index():
    return redirect(url_for('home',content="home"))
@app.route('/home',methods=["GET","POST"])
def home():
    #0 if the user is not logged in
    #1 if the user is logged in
    content = request.args.get('content')
    return render_template('main.html',page_content=content),200
@app.route('/home/success')
def success():
    page_content = request.args.get('page_content') 
    username = request.args.get('username')
    return render_template('main-login-success.html',page_content=page_content,username=username)
@app.route('/home/logout',methods=['POST','GET'])
def logout():
    content = request.args.get('content')
    return redirect(url_for('home',content=content))
@app.route('/home/register', methods=["GET","POST"])
def register():
    randnum = random.randint(100000,999999)
    key = c.generate()
    content = request.args.get('content')
    hotel = request.form.get('hotel')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    #returns to the home page accessed randomly
    if hotel == None and email == None and password == None and email == None and password == None:
        return redirect(url_for('home',content="home"),code=200)
    else:
        #returns to the page they were currently viewing
        hot = Hotel()
        r = rsaDB()
        keys = c().generate()
        r.insert(keys["private"],keys["public"],email)
        data = {"hotel" : c().encrypt(hotel,keys["public"]), "fullname" : c().encrypt(fullname,keys["public"]),"email" : c().encrypt(email,keys["public"]), "password" : c().encrypt(password,keys["public"])}
        hot.insert(data["hotel"],data["fullname"],data["email"],data["password"],randnum)
        r.insert(key['private'],key['public'],email)
        return redirect(url_for('home',content=content,register=True),code=302)
@app.route('/login', methods=["GET","POST"])
def login():
    
    content = request.args.get('content')
    email = request.form.get('email')
    passw = request.form.get('password')
    if content == None and email == None and passw == None:
        return "<h1>INVALID ACCESS!</h1>"
    return redirect(url_for('home/success',content=content))
@app.route('/home/verify')
def verify():
    otp = request.args.get('otp')
    email = request.args.get('email')
    if otp == None and email == None:
        #redirects to the home page when accessed directly
        return redirect(url_for('home',content='home'))
    return redirect(url_for('home',content='home')) 

if __name__ == '__main__':
    app.run(debug=True)
class rsaDB(object):
    __dbname = "hotelDRRating"
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
                cursor.execute("CREATE TABLE IF NOT EXISTS rsakeys(_id INTEGER AUTO_INCREMENT PRIMARY KEY, _privateKey VARCHAR(2000) NOT NULL, _publicKey VARCHAR(2000) NOT NULL,_email TEXT NOT NULL)")
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
    def insert(self,hotel:str,fullname:str,email:str,password:str,otp:int):
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            with conn.cursor() as cursor:
                sql = f"INSERT INTO `hotelinfo`(_hotel,_fullname,_email,_password,_otp,_verified) VALUES('{hotel}','{fullname}','{email}','{password}',{otp},0);"
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
        rsadb = rsaDB()
        conn=psql.connect(host='localhost',user='root',password='',database=self.__dbname)
        try:
            keys = rsadb.getKeys(email=email)
            email = c().encrypt(email,keys["public"])
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
class rsa(object):
    def __init__(self):
        return
    def generate(self,keysize=2048):
        key = RSA.generate(keysize)
        privatekey = key.export_key()
        publickey = key.public_key().export_key()
        return {"public" : publickey, "private" : privatekey.decode()}
    def encrypt(self,msg,pubkey):
        publickey = RSA.importKey(pubkey)
        cipher = PKCS1_v1_5.new(publickey)
        return b64.b64encode(cipher.encrypt(msg.encode('ascii'))).decode('ascii')
    def decrypt(self,msg,privkey):
        privatekey = RSA.importKey(privkey)
        cipher = PKCS1_v1_5.new(privatekey)
        return cipher.decrypt(b64.b64decode(msg), Random.new().read(20+SHA.digest_size)).decode('utf-8')