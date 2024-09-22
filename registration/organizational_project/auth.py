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
    email = request.form.get('email')
    FirstName  = request.form.get('FirstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 2:
        #if email address does not contain either @gmail.con or @yahoo.com
        flash('Email must be greater than 4 characters.')
        pass
    if len(FirstName) < 2:
        pass
    if len(password1) == len(password2):
        pass
    
    return render_template('sign_up.html')
