'''helps break your code to various smaller portions'''
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    '''this is the home route'''
    return render_template('home.html')
