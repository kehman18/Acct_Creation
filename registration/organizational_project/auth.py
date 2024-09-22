'''helps break your code to various smaller portions'''
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''responsible for user login'''
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    '''responsible for user logout'''
    return "<p>logout successful</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''this function is responsible for user sign-up'''
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName  = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(FirstName) < 2:
            flash('firstname must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('password do not match', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 6 characters.', category='error')
        else:
            flash('Account Created Successfully', category='success')
        
    return render_template('sign_up.html')
