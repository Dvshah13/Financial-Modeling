from flask import Flask, request, session, redirect, render_template
from flask.ext.bcrypt import Bcrypt
import logging
from mongoengine import *
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)

# MongoDB Database connection
connect('financial_modeling', host='localhost', port=27017)

# Different Mongo collections/tables
class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(max_length=50)
    password = StringField(max_length=200)
    cdate = DateTimeField(default=datetime.datetime.now)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/submit', methods=['GET', 'POST'])
def register():
    new_user = User (
            first_name = request.form['fname'],
            last_name = request.form['lname'],
            email = request.form['email'],
            password = bcrypt.generate_password_hash(request.form['password'])
            )
    print new_user
    new_user.save()
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    new_user = User.objects.get(email = request.form['email'])
    print new_user.first_name
    if (bcrypt.check_password_hash(new_user.password, request.form['password'])):
        print new_user.first_name
        return new_user.first_name
    else:
        return "Wrong Password"

if __name__ == '__main__':
    app.run(debug = True)
