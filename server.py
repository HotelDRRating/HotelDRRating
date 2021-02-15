from flask import Flask,redirect,url_for,render_template,request,render_template_string
import response_send as rs
from db import hotel_info
import html_source as hh

__NULL__ = ""
app = Flask(__name__)

@app.route('/send_appreciation/_<string:test>')
def send_appreciation(test):
   
    return "<h1>"+test+"</h1>"

@app.route('/',methods=["GET","POST"])
def main():
    if request.method=="GET":
        return render_template('main.html')
    return render_template('main.html'),200
@app.route('/register_user_hotel', methods=["GET","POST"])
def register_user_hotel():
    h = hotel_info()
    if request.method == "POST":
        hotel = request.form.get('hotel')
        fname = request.form.get('fullname')
        email = request.form.get('email')
        passw = request.form.get('password')
        h.insert(hotel,fname,email,passw)
        
    return redirect(url_for('main.html'))

@app.route('/register_success')
def register_success():
    return __NULL__
if __name__ == '__main__':
    app.run(debug=True)
    



