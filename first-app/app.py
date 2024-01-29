from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password123",
  database="test",
  auth_plugin='mysql_native_password'
)

print(mydb)

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] =

@app.route('/Hello')
def hello():
    return "Hello World!"

@app.route('/Index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)