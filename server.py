from flask import Flask,redirect,url_for,render_template,request,session
from datetime import timedelta
import crypto, hoteldb,rsadb,pymysql as psql
__dbname = "hotelDRRating"
app = Flask(__name__)
app.secret_key="b5c6c1c36670443727988e3edb14725f19b6233937f3ec9ff09f7b8185b92c7beda60d6b17de3b27c46a721834f5cbb1c5b0275c0743a893d9d9de026761cbd9"
app.permanent_session_lifetime = timedelta(minutes=30)
@app.route('/',methods=["GET","POST"])
def index():
    conn=psql.connect(host='localhost',user='root',password='')
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {__dbname}")
    finally:
        conn.close()
    rsadb.create_table()
    hoteldb.create_table()
    session["hotel"] = "b5c6c1c36670443727988e3edb14725f19b6233937f3ec9ff09f7b8185b92c7beda60d6b17de3b27c46a721834f5cbb1c5b0275c0743a893d9d9de026761cbd9"
    return redirect(url_for('home',content="home"))
@app.route('/home',methods=["GET","POST"])
def home():
    content = request.args.get('content')
    return render_template('main.html',page_content=content),200
@app.route('/home/success')
def success():
    page_content = request.args.get('page_content') 
    return render_template('main-login-success.html',page_content=page_content)

@app.route('/login', methods=['POST','GET'])
def login():
    #may possibly changed
    content = request.args.get('content')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed = crypto.hash(email+password)
    keys = rsadb.getKeys(hashed)
    private = keys["private"]
    info = hoteldb.get(hashed)
    if email == crypto.decrypt(info["email"],private) and password == crypto.decrypt(info["password"]) and hashed == info["hash"]:
        session["fullname"] = info["fullname"]
        session['hotel'] = info["hotel"]
        return redirect(url_for('home',content=content))
@app.route('/register', methods=['POST','GET'])
def register():
    #may possibly changed
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    hotel= request.form.get('hotel')
    password = request.form.get('password')
    content = request.args.get('content')
    hashed = crypto.hash(email+password)
    keys = crypto.generate()
    rsadb.insert(keys['private'], keys['public'],hashed)
    data = [crypto.encrypt(hotel,keys['public']),crypto.encrypt(fullname,keys['public']),crypto.encrypt(email,keys['public']),crypto.encrypt(password,keys['public']),crypto.hash(email+password)]
    hoteldb.insert(data[0],data[1],data[2],data[3],data[4])
    return redirect(url_for('home',content=content))
@app.route('/verify')
def verify():
    hash = request.args.get('hash')
    return str(hash)
@app.route('/logout',methods=["GET","POST"])
def logout():
    content = request.args.get('content')
    session.pop('email', None)
    return redirect(url_for('home',content=content))
if __name__ == '__main__':
    app.run(debug=True)