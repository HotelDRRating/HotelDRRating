from flask import Flask,redirect,url_for,render_template,request
import RSA as rsa, random
__NULL__ = ""
app = Flask(__name__)

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
    key = rsa.generate_key()
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
        return redirect(url_for('home',content=content),code=302)
@app.route('/login', methods=["GET","POST"])
def login():
    
    content = request.args.get('content')
    email = request.form.get('email')
    passw = request.form.get('password')
    if content == None and email == None and passw == None:
        return "<h1>INVALID ACCESS!</h1>"
    else:

        if True:
            return redirect(url_for('home/success',content=content))
        else:
            return "<h1> LOGIN FAILED </H1>"
'''
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