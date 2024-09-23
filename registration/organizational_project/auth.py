'''helps break your code to various smaller portions'''
from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''responsible for user login'''
    #check for the email address if available
    #if yes, check the password.
    #if yes, login to the acct
    #if email not found, direct the person to login
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    '''responsible for user logout'''
    return "<p>logout successful</p>"

def validate_email(user_email):
    '''this function is to validate the email address of the user'''
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    email_domain = ['gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com', 'icloud.com', 'zoho.com', 'aol.com', 'yandex.com']
    
    if user_email is None or not isinstance(user_email, str):
        return 'Email is required'
    
    pattern_check = re.match(email_regex, user_email)
    domain = user_email.split('@')[-1]

    if pattern_check:
        if domain in email_domain:
            return None
        else:
            return 'This email domain is not accepted'
    else:
        return 'Invalid email format'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''this function is responsible for user sign-up'''
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName  = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_validation_result = validate_email(email)
        if email_validation_result is not None:
            return render_template('sign_up.html', error=email_validation_result)

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
