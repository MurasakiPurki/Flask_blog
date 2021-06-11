from enum import unique
from blog import db

class User(db.Model):
    userNum = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(200), unique=True, nullable = False)
    userPass = db.Column(db.String(200), nullable = False)
    name = db.Column(db.String(20), nullable = False)

class Post(db.Model):
    postID = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

