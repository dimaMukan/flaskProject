from flask import Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=["GET","Post"])
def log_in():
    return render_template("login.html", text='text',user='Tim',boolean=True)

@auth.route('/logout')
def log_out():
    return render_template("home.html")

@auth.route('sign-up')
def sign_up():
    return render_template("sign_up.html",methods=["GET","Post"])
