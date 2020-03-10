from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def login():
    print(request.is_json)
    content = request.get_json()
    print(content["username"])
    print(content["token"])
    return "ALL GOOD"

if __name__ == "__main__":
	app.run(host='192.168.0.102', port=4000, debug=True)