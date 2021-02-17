from flask import Flask,redirect,url_for,render_template,request,render_template_string
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
@app.route('/')
def index():
    return redirect('/home', code=302)
@app.route('/home',methods=["GET","POST"])
@app.route('/home/<int:login>/<string:username>')
def home(login=0,username=__NULL__):
    #0 if the user is not logged in
    #1 if the user is logged in
    if login == 0 and username == __NULL__:
        return render_template('main.html'),200
    else:
        return render_template('main-login-success.html',username=username),200
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
            return redirect('/home')
if __name__ == '__main__':
    app.run(debug=True)