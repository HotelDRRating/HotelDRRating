from flask import Flask,redirect,url_for,render_template,request
from scripts import *
__NULL__ = ""
app = Flask(__name__)

@app.route('/send_appreciation/')
def send_appreciation(test):
    email = request.form.get('email')
    msg = request.form.get('message')
    mailer = emailing()
    mailer.send_thank_you(email=email)
    return redirect('/contact_us')
@app.route('/',methods=["GET","POST"])
def index():
    return redirect(url_for('home',content="home",isloggedin=0))
@app.route('/home',methods=["GET","POST"])
def home():
    #0 if the user is not logged in
    #1 if the user is logged in
    content = request.args.get('content')
    isloggedin = request.args.get('isloggedin')
    username = request.args.get('username')
    return render_template('main.html',page_content=content,isloggedin=isloggedin,username=username),200
@app.route('/register',methods=["GET","POST"])
def register():
    hotel = request.args
'''
@app.route('/register_user_hotel', methods=["GET","POST"])
def register_user_hotel():
    if request.method == "POST":
        hotel = request.form.get('hotel')   
        fname = request.form.get('fullname')
        email = request.form.get('email')
        passw = request.form.get('password')
        x = crypto()
        x.generate(user=email)
    return redirect('/main',code=302)
@app.route('/login-auth', methods=["GET","POST"])
def login_auth():
    if request.method == "POST":
        hotel = hotelDB()
        email = request.form.get('email')
        passw = request.form.get('password')
        if hotel.login_auth(email, passw):
            return redirect('/main')
'''
if __name__ == '__main__':
    app.run(debug=True)