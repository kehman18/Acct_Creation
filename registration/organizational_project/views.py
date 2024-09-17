'''helps break your code to various smaller portions'''
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    '''this is the home route'''
    return '<h1>Test<h1>'