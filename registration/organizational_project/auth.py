'''helps break your code to various smaller portions'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login successful</p>"

@auth.route('/logout')
def logout():
    return "<p>logout successful</p>"
