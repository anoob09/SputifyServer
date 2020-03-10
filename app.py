from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/user/', methods=['GET', 'POST'])
def login():
    print(request.form['user'])
    print(request.form['token'])




if __name__ == "__main__":
	app.run(host='0.0.0.0', port=4000, debug=True)