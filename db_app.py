from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://anoob09@localhost:3306/sputify'
db = SQLAlchemy(app)
class Users(db.Model):
    userId = db.Column(db.String(30), primary_key=True)
    token = db.Column(db.String(255), unique = True, nullable = False)
    refreshToken = db.Column(db.String(255), unique = True, nullable = False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
