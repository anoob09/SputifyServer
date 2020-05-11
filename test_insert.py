from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from db_app import db
from db_app import Users

test = Users(userId = "anoob1", token = "jsakdhkasjhdsi24r3892f", refreshToken = "sjdf9832fiasda", latitude = 42.3243, longitude = 90.8348)
# db.create_all()
db.session.add(test)
db.session.commit()