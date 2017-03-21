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

# MongoDB Database connection Locally
connect('financial_modeling', host='localhost', port=27017)

# MongoDB Remote hosting
# app.config["MONGODB_DB"] = 'deepak_db'
# connect(
#     'deepak_db',
#     username='dvshah13',
#     password='rockets13',
#     host='mongodb://<dvshah13>:<rockets13>@ds161099.mlab.com:61099/deepak_db',
#     port=61099
# )

# Different Mongo collections/tables
class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(max_length=50)
    password = StringField(max_length=200)
    cdate = DateTimeField(default=datetime.datetime.now)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/register_page')
def register_page():
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
    session['email'] = new_user.email
    session['first_name'] = new_user.first_name
    if (bcrypt.check_password_hash(new_user.password, request.form['password'])):
        print new_user.first_name
        return render_template('portfolio_dashboard.html', email = session.get('email'), first_name = session.get('first_name'))
    else:
        return "Wrong Password, click back to try again."

@app.route('/stock_data', methods=['POST'])
def stockInfo():
    data = request.json
    stock = data['stock_symbol']
    session['stock'] = stock
    print stock
    return "Worked"

@app.route('/stock_data/d1', methods=['GET'])
def get_data_scripts():
    symbol = session.get('stock')
    print symbol
    import basic_stock_data
    ret = basic_stock_data.data_front_page(symbol)
    print ret
    #return in json format
    return jsonify(ret)

@app.route('/stock_data/d2', methods=['GET'])
def get_rsi_scripts():
    symbol = session.get('stock')
    print symbol
    import rsi_data
    ret = rsi_data.read_stock_rsi(symbol)
    print ret
    #return in json format
    return jsonify(ret)

@app.route('/stock_data/d3', methods=['GET'])
def get_twitter_scripts():
   symbol = session.get('stock')
   import twitter_sentiment
   ret = twitter_sentiment.findStock(symbol)
   print ret
   #return in json format
   return jsonify(ret)
#
@app.route('/stock_data/d4', methods=['GET'])
def get_daily_algo_scripts():
   symbol = session.get('stock')
   import daily_stock_prediction
   ret = daily_stock_prediction.stock_data(symbol)
   print ret
   #return in json format
   return jsonify(ret)

@app.route('/stock_data/d5', methods=['GET'])
def get_weekly_algo_scripts():
   symbol = session.get('stock')
   import weekly_stock_predictor
   ret = weekly_stock_predictor.stockData(symbol)
   print ret
   #return in json format
   return jsonify(ret)
#
@app.route('/stock_data/d6', methods=['GET'])
def get_monthly_algo_scripts():
   symbol = session.get('stock')
   import monthly_stock_predictor
   ret = monthly_stock_predictor.stockData(symbol)
   print ret
   #return in json format
   return jsonify(ret)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()
