'''helps break your code to various smaller portions'''
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    '''responsible for user login'''
    return render_template('login.html')

@auth.route('/logout')
def logout():
    '''responsible for user logout'''
    return "<p>logout successful</p>"

@auth.route('/sign-up')
def sign_up():
    '''this function is responsible for user sign-up'''
    return render_template('sign_up.html')
