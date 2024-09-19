'''helps break your code to various smaller portions'''
from flask import Blueprint, render_template, request

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
    return render_template('sign_up.html')
