'''this is a flask app for my server'''
from flask import Flask

def create_app():
    '''this is the function that should be able to be called from main.py'''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'love'
    
    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app