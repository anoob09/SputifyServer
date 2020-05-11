from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost:3306/sputify'
db = SQLAlchemy(app)
refreshTokenURL = "https://accounts.spotify.com/api/token"
# client_id = 


@app.route('/', methods=['POST']) 
def login():
    content = request.get_json()
    code = content["code"]
    latitude = content["latitude"]
    longitude = content["longitude"]
    import requests

    # Get access_token and refresh_token using authorization_code
    headers = {
        'Authorization': 'Basic MGVkNjlhMTNmNDMyNGIxZmEwMmE0Y2YyNmExMWJiYTk6ZTI2MTJkOTFiMGM5NGE4MDg3NzJhMWI5M2NiM2IyYzk=',
    }

    data = {
      'grant_type': 'authorization_code',
      'code': code,
      'redirect_uri': 'https://eflask-app-1.herokuapp.com/'
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    token_json = response.json()
    token = token_json["access_token"]
    refresh_token = token_json["refresh_token"]

    # Get user profile details using access_token

    headers = {
        'Authorization': 'Bearer '+ token,
    }

    response = requests.get('https://api.spotify.com/v1/me', headers=headers)

    print(response.json())


    return "ALL GOOD"

if __name__ == "__main__":
	app.run(host='192.168.43.57', port=5000, debug=True)
