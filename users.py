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
        return "Wrong Password, click back to try again."

@app.route('/stock_data', methods=['POST'])
def stockInfo():
    data = request.json
    stock = data['stock_symbol']
    session['stock'] = stock
    print stock
    return "Yes"

# @app.route('/stock_data', methods=['GET'])
# def get_data_scripts():
#     symbol = session.get('stock')
#     import basic_stock_data
#     session['data_set1'] = basic_stock_data.data_front_page(symbol)
#     # session['data_set2'] = basic_stock_data.define_stock_rsi(symbol)
#     results_set1 = session.get('data_set1')
#     # results_set2 = session.get('data_set2')
#     print results_set1['current_price']
#     # print results_set2['rsi_change_50_10']
#     import daily_stock_prediction
#     session['data_set2'] = daily_stock_prediction.stockData(symbol)
#     results_set2 = session.get('data_set2')
#     print results_set2['predicted']
#     return "Worked"

@app.route('/stock_data/d1', methods=['GET'])
def get_data_scripts():
   symbol = session.get('stock')
   import basic_stock_data
   var ret = basic_stock_data.data_front_page(symbol)
   #return in json format
   return res.send(ret)

@app.route('/stock_data/d2', methods=['GET'])
def get_data_scripts():
   symbol = session.get('stock')
   import twitter_sentiment
   var ret = twitter_sentiment.findStock(symbol)
   #return in json format
   return res.send(ret)

@app.route('/stock_data/d3', methods=['GET'])
def get_data_scripts():
   symbol = session.get('stock')
   import daily_stock_prediction
   var ret = daily_stock_prediction.stock_data(symbol)
   #return in json format
   return res.send(ret)

@app.route('/stock_data/d4', methods=['GET'])
def get_data_scripts():
   symbol = session.get('stock')
   import weekly_stock_predictor
   var ret = weekly_stock_prediction.stockData(symbol)
   #return in json format
   return res.send(ret)

@app.route('/stock_data/d5', methods=['GET'])
def get_data_scripts():
   symbol = session.get('stock')
   import monthly_stock_predictor
   var ret = monthly_stock_prediction.stockData(symbol)
   #return in json format
   return res.send(ret)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
