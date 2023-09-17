from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def log_in():
    return '<p>Log in</p>'
@auth.route('/logout')
def log_out():
    return '<p>Logout</p>'

@auth.route('sign-up')
def sign_up():
    return '<p>Sign Up</p>'
