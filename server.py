from flask import Flask,redirect,url_for,render_template,request,session
from datetime import timedelta
import crypto,hoteldb,rsadb,pymysql as psql,response_send,bleach
__dbname = "hotelDRRating"
app = Flask(__name__)
app.secret_key=crypto.hash("hotelDRRating")
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
    return redirect(url_for('home',content="home"))
@app.route('/home',methods=["GET","POST"])
def home():
    content = request.args.get('content')
    session.modified = True
    if 'fullname' in session and 'email' in session:
        return render_template('main.html',page_content=content,user = session.get('fullname'), email = session.get('email'),hotel = session.get('hotel'), password = session.get('password'))
    
    return render_template('main.html',page_content=content,user=None)
@app.route('/login', methods=['POST','GET'])
def login():
    content = request.args.get('content')
    email = request.form.get('email')
    password = request.form.get('password')
    if content is None and email is None and password is None:
        return redirect(url_for('home',content='home'))
    hashed = crypto.hash(email+password)
    keys = rsadb.getKeys(hashed)
    private = keys["private"]
    info = hoteldb.get(hashed)
    if email == crypto.decrypt(info["email"],private) and password == crypto.decrypt(info["password"],private) and hashed == info["hash"]:
        session["email"] = crypto.decrypt(info["email"],private)
        session["password"] = crypto.decrypt(info["password"],private)
        session['hotel'] = crypto.decrypt(info["hotel"],private)
        session['fullname'] = crypto.decrypt(info["fullname"],private)
        return redirect(url_for('home',content=content))
@app.route('/contact', methods=["GET","POST"])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    response_send.send_appreciation_email(name, email)
    return redirect(url_for('home',content='contact_us'))
@app.route('/register', methods=['POST','GET'])
def register():
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    hotel= request.form.get('hotel')
    password = request.form.get('password')
    content = request.args.get('content')
    hashed = crypto.hash(email+password)
    keys = crypto.generate()
    rsadb.insert(keys['private'], keys['public'],hashed)
    data = [crypto.encrypt(bleach.clean(hotel),keys['public']),crypto.encrypt(bleach.clean(fullname),keys['public']),crypto.encrypt(bleach.clean(email),keys['public']),crypto.encrypt(bleach.clean(password),keys['public']),crypto.hash(email+password)]
    hoteldb.insert(data[0],data[1],data[2],data[3],data[4])
    response_send.send_register(email,fullname,hashed)
    return redirect(url_for('home',content=content))
@app.route('/verify')
def verify():
    hash = request.args.get('hash')
    if hash is None:
        return redirect(url_for('home',content='home'))
    hoteldb.verify(hash)
    return redirect(url_for('home',content='home'))
@app.route('/logout',methods=["GET","POST"])
def logout():
    content = request.args.get('content')
    session.pop('email', None)
    session.pop('fullname', None)
    session.pop('hotel', None)
    session.pop('password', None)

    return redirect(url_for('home',content=content))
@app.route('/update', methods=["GET","POST"])
def update():
    return "<h1>Sorry But This part is still work in progress. Please come back at a later date</h1>"
@app.route('/assessment' , methods=["GET","POST"])
def assessment():
    return "<h1>Sorry But This part is still work in progress. Please come back at a later date</h1>"
if __name__ == '__main__':
    app.run(debug=True)