import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from src import utils

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://senapati:senapati@localhost:3306/sputify'
db = SQLAlchemy(app)

class Users(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    refreshToken = db.Column(db.String(255), unique = True, nullable = False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String(50))

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print('not inserted')



@app.route('/', methods=['POST'])
def sign_up():
    try:
        content = request.get_json()
    except Exception:
        return utils.get_error_response(400, "body not in json format")
    try:
        accessCode = content["accessCode"]
        # username = content["username"]
        # token = content["token"]
        # refreshToken = content["refreshToken"]
        latitude = content["latitude"]
        longitude = content["longitude"]
    except KeyError as e:
        return utils.get_error_response(400, e)
    city = utils.get_location_from_lat_long(latitude, longitude)

    newUser = Users(username=username, token=token, refreshToken=refreshToken,
          latitude=latitude, longitude=longitude, city=city)
    newUser.add()
    return utils.get_success_response()


def initialize_database():
    db.create_all()

if __name__ == "__main__":
    initialize_database()
    app.run(host='0.0.0.0', debug=True)
