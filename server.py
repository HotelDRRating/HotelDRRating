from flask import Flask,redirect,url_for,render_template,request,render_template_string

__NULL__ = ""
app = Flask(__name__)

@app.route('/send_appreciation/_<string:test>')
def send_appreciation(test):
   
    return "<h1>"+test+"</h1>"
@app.route('/')
def index():
    return redirect('/home', code=302)
@app.route('/home',methods=["GET","POST"])
@app.route('/home/<int:login>/<string:username>')
def home(login=0,username=__NULL__):
    #0 if the user is not logged in
    #1 if the user is logged in
    if login is 0 and username is __NULL__:
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
        
        
    return redirect('/main',code=302)

if __name__ == '__main__':
    app.run(debug=True)
    



