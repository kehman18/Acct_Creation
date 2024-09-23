from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    '''this is the function that should be able to be called from main.py'''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'love'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(path.dirname(__file__), DB_NAME)}'
    
    db.init_app(app)
    
    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists(path.join(path.dirname(__file__), DB_NAME)):
        with app.app_context():
            db.create_all()
            print('Created Database!')
