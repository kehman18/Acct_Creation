from . import db
from flask_login import UserMixin


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.string(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.string(150), unique=True)
    password = db.Column(db.string(150))
    first_name = db.Column(db.string(150))
    notes = db.relationship('Note')