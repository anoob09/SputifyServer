from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
import os
import requests
from db_app import Users1
from db_app import db
from db_app import app

refreshTokenURL = "https://accounts.spotify.com/api/token"
client_id = 'MGVkNjlhMTNmNDMyNGIxZmEwMmE0Y2YyNmExMWJiYTk6ZTI2MTJkOTFiMGM5NGE4MDg3NzJhMWI5M2NiM2IyYzk='
db.create_all()

@app.route('/', methods=['POST']) 
def login():
    content = request.get_json()
    code = content["code"]
    latitude = content["latitude"]
    longitude = content["longitude"]
    import requests

    # Get access_token and refresh_token using authorization_code
    headers = {
        'Authorization': 'Basic '+ client_id,
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
    user_data_json = response.json()
    user_id = user_data_json["id"]

    # Remove user if already present in Databse
    user = Users1.query.filter_by(userid='anoob1').first()
    if user is not None:
        Users1.query.filter_by(userid=user_id).delete()
        db.session.commit()
    new_user = Users1(userid = user_id, refreshtoken = refresh_token, latitude = latitude, longitude = longitude, city = "mumbai")
    db.session.add(new_user)
    db.session.commit()

    # Get all users from Database and get details of all the users
    users = Users1.query.all()
    for user in users:
        user_refresh_token = user.refreshtoken

    #     headers = {
    #         'Authorization': 'Basic ' + client_id,
    #     }

    #     data = {
    #       'grant_type': 'refresh_token',
    #       'refresh_token': user_refresh_token 
    #     }

    #     response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    #     refreshed_token_json = response.json()
    #     print(refreshed_token_json)

    return "ALL GOOD"

if __name__ == "__main__":
	app.run(host='192.168.43.57', port=5000, debug=True)
