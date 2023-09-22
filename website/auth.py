from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=["GET","Post"])
def log_in():
    data = request.form
    print(data)
    return render_template("login.html", text='text',user='Tim',boolean=True)

@auth.route('/logout')
def log_out():
    return render_template("home.html")

@auth.route('sign-up',methods=["GET","Post"])
def sign_up():
    if request.method == 'POST':
        data = request.form
        print(data)
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('Email must be more than 4 characters', category='Error')
        elif len(first_name)<2:
            flash('First name must be more than 1 characters', category='Error')
        elif len(password1)<7:
            flash('Password must be more than 6 characters', category='Error')
        elif password1 != password2:
            flash('Passwords don`t match', category='Error')
        else:
            flash('Account created!',category='Success')




    return render_template("sign_up.html")
