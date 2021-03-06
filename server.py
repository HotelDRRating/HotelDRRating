from flask import Flask,redirect,url_for,render_template,request
import random,pymysql as psql
import crypto,rsadb
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
    if request.form.get('hotel') == None and request.form.get('fullname') == None and request.form.get('email') == None and request.form.get('password'):
        return redirect(url_for('home',content='home'))
    content = request.args.get('content')

    hoteldb = Hotel()
    keys = crypto.generate()
    publickey = keys["public"]
    privatekey = keys["private"]
    hotel = request.form.get('hotel')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    rsadb.insert(privatekey,publickey,email)
    data = {'hotel': crypto.encrypt(hotel,publickey),'fullname': crypto.encrypt(fullname),'email': crypto.encrypt(email,publickey),'password': crypto.encrypt(password,publickey),'hash':hash.hash(email+password)}
    if hoteldb.insert(data['hotel'],data['fullname'],data['email'],data['password'],data['hash']):
        return redirect(url_for('home',content=content))
    else:
        return "<h1>500 Internal Server Error</h1>"

@app.route('/home/login', methods=["GET","POST"])
def login():
    
    content = request.args.get('content')
    email = request.form.get('email')
    passw = request.form.get('password')
    if content == None and email == None and passw == None:
        return "<h1>INVALID ACCESS!</h1>",redirect(url_for('home',content="home"))
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
class Hotel(object):
    __dbname = "hotelDRRating"
    def __init__(self):
        return
   
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

