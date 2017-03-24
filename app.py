from flask import Flask, request, session, redirect, render_template, jsonify, make_response
from flask.ext.bcrypt import Bcrypt
import logging
from mongoengine import *
import datetime
from flask_restful import reqparse
import json

import random
import StringIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv
import pandas as pd


app = Flask(__name__)
app.secret_key = 'whoathere'
bcrypt = Bcrypt(app)

# MongoDB Database connection Locally
# connect('financial_modeling', host='localhost', port=27017)

# MongoDB Remote hosting
app.config["MONGODB_DB"] = 'deepak_db'
connect(
    'deepak_db',
    username='dvshah13',
    password='rockets13',
    host='mongodb://dvshah13:rockets13@ds161099.mlab.com:61099/deepak_db',
    port=61099
)


# Different Mongo collections/tables
class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(max_length=50, unique=True)
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

@app.route('/profile', methods=['GET', 'POST'])
def update_page():
    update_user = User.objects.get(email = session.get('email'))
    session['email'] = update_user.email
    session['first_name'] = update_user.first_name
    session['last_name'] = update_user.last_name
    session['password'] = update_user.password
    return render_template('profile_page.html', email = session.get('email'), first_name = session.get('first_name'), last_name = session.get('last_name'), password = session.get('password'))

@app.route('/submit_profile', methods=['GET', 'POST'])
def update():
    update_user = User (
            first_name = request.form['fname'],
            last_name = request.form['lname'],
            email = request.form['email'],
            password = bcrypt.generate_password_hash(request.form['password'])
            )
    session['email'] = update_user.email
    session['first_name'] = update_user.first_name
    print new_user
    update_user.save()
    return render_template('portfolio_dashboard.html', email = session.get('email'), first_name = session.get('first_name'))

@app.route('/stock_data', methods=['POST'])
def stockInfo():
    data = request.json
    stock = data['stock_symbol']
    session['stock'] = stock
    print stock
    return "Worked"

@app.route('/figure', methods=['GET'])
def figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    # pd.read_csv('/app/daily_historical_prices/spy.csv', nrows=10)
    df = pd.read_csv('/app/daily_historical_prices/spy.csv', nrows=20)
    date_graph = pd.to_datetime(df['Date'])
    adj_close = df['Adj Close']
    xs = date_graph
    ys = adj_close
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/stock_data/d1', methods=['GET'])
def get_data_scripts():
    symbol = request.args['stock_symbol']
    print symbol
    import basic_stock_data
    ret = basic_stock_data.data_front_page(symbol)
    #return in json format
    return jsonify(ret)

@app.route('/stock_data/d2', methods=['GET'])
def get_rsi_scripts():
    symbol = request.args['stock_symbol']
    print symbol
    import rsi_data
    ret = rsi_data.read_stock_rsi(symbol)
    #return in json format
    return jsonify(ret)

@app.route('/stock_data/d3', methods=['GET'])
def get_twitter_scripts():
    symbol = request.args['stock_symbol']
    print symbol
    import twitter_sentiment
    ret = twitter_sentiment.findStock(symbol)
    #return in json format
    return jsonify(ret)
#
@app.route('/stock_data/d4', methods=['GET'])
def get_daily_algo_scripts():
    symbol = request.args['stock_symbol']
    import daily_stock_prediction
    ret = daily_stock_prediction.stock_data(symbol)
    print symbol
    #return in json format
    return jsonify(ret)

@app.route('/stock_data/d5', methods=['GET'])
def get_weekly_algo_scripts():
    symbol = request.args['stock_symbol']
    import weekly_stock_predictor
    ret = weekly_stock_predictor.stockData(symbol)
    print symbol
    #return in json format
    return jsonify(ret)
#
@app.route('/stock_data/d6', methods=['GET'])
def get_monthly_algo_scripts():
    symbol = request.args['stock_symbol']
    import monthly_stock_predictor
    ret = monthly_stock_predictor.stockData(symbol)
    print symbol
    #return in json format
    return jsonify(ret)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()
