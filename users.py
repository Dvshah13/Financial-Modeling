from flask import Flask, request, session, redirect, render_template, jsonify
from flask.ext.bcrypt import Bcrypt
import logging
from mongoengine import *
import datetime
from flask_restful import reqparse
import json

app = Flask(__name__)
app.secret_key = 'whoathere'
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
    return render_template('login.html')

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
    session['email'] = new_user.email
    session['first_name'] = new_user.first_name
    if (bcrypt.check_password_hash(new_user.password, request.form['password'])):
        print new_user.first_name
        return render_template('portfolio_dashboard.html', email = session.get('email'), first_name = session.get('first_name'))
    else:
        return "Wrong Password"

@app.route('/stock_data', methods=['GET', 'POST'])
def stockInfo():
    if request.method == 'POST':
        data = request.json
        stock = data['stock_symbol']
        print data

    return 'Yes'

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
