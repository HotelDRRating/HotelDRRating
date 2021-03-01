<<<<<<< HEAD
from flask import Flask,redirect,url_for,render_template,request,flash,session
import random
from db import Hotel,rsaDB
from CRYPT import c
=======
from flask import Flask,redirect,url_for,render_template,request
import RSA as rsa, random
>>>>>>> dceefc773b03aee368a55281dbe3a84fc78a024e
__NULL__ = ""
app = Flask(__name__)
CRYPT = c()
@app.route('/contact_us')
def contact_us():
    #insert logic here
    return redirect(url_for('home',content="contact_us"))
@app.route('/',methods=["GET","POST"])
def index():
    return redirect(url_for('home',content="home"))
@app.route('/home',methods=["GET","POST"])
def home():
    #0 if the user is not logged in
    #1 if the user is logged in
    content = request.args.get('content')
    email = request.form.get('email')
    password = request.form.get('password')
    if email is not None and password is not None:
        xx = []
        for x in list(email):
            if x == '@':
                break
            xx.append(x)
        return redirect(url_for('home/success',page_content=content,username="".join(xx),isloggedin=1))
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
    key = CRYPT.generate()
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
        keys = CRYPT.generate()
        r.insert(keys["private"],keys["public"],email)
        data = {"hotel" : CRYPT.encrypt(hotel,keys["public"]), "fullname" : CRYPT.encrypt(fullname,keys["public"]),"email" : CRYPT.encrypt(email,keys["public"]), "password" : CRYPT.encrypt(password,keys["public"])}
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
    return 'VERIFIED'

if __name__ == '__main__':
    app.run(debug=True)