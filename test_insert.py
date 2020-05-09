from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from db_app import db
from db_app import Users

test = Users(userId = "anoob", token = "jsakdhkasjhdsi24r3892fh", refreshToken = "sjdf9832fiasdad", latitude = 42.32432, longitude = 90.83248)
db.create_all()
db.session.add(test)
db.session.commit()