import csv
import pandas as pd
from yahoo_finance import Share
# from mongoengine import *
# import datetime

# MongoDB Database connection
# connect('financial_modeling', host='localhost', port=27017)

# Different Mongo collections/tables
# class User(Document):
#     name = StringField(required=True, max_length=200)
#     email = StringField(required=True, unique=True)
#     password = StringField(required=True, max_length=50)
#     cdate = DateTimeField(default=datetime.datetime.now)
#
# class User_portfolio(Document):
#     email = StringField(required=True, unique=True)
#     stock_name = ListField(required=True, max_length=200)


# Get current data of stock from Yahoo Finance
def current_data(stock):
    if stock == 'aapl':
        symbol = Share('AAPL')
        data_front_page(stock, symbol)
    elif stock == 'goog':
        symbol = Share('GOOG')
        data_front_page(stock, symbol)
    elif stock == 'spy':
        symbol = Share('SPY')
        data_front_page(stock, symbol)
    elif stock == 'fb':
        symbol = Share('fb')
        data_front_page(stock, symbol)
    elif stock == 'amzn':
        symbol = Share('AMZN')
        data_front_page(stock, symbol)
    elif stock == 'dis':
        symbol = Share('dis')
        data_front_page(stock, symbol)
    elif stock == 'msft':
        symbol = Share('msft')
        data_front_page(stock, symbol)

def data_front_page(stock, symbol):
    print stock, "current price: ", symbol.get_price()
    print stock, "day percent change: ", symbol.get_percent_change()
    print stock, "daily volume: ", symbol.get_volume()
    print stock, "EBITDA: ", symbol.get_ebitda()
    print stock, "50 day sma: ", symbol.get_50day_moving_avg()
    print stock, "percent change from 50 day sma: ", symbol.get_percent_change_from_50_day_moving_average()
    print stock, "price to earnings ratio: ", symbol.get_price_earnings_ratio()
    print stock, "price to earnings growth ratio: ", symbol.get_price_earnings_growth_ratio()
    print stock, "short ratio: ", symbol.get_short_ratio()

# Add a new user
# def add_user():
#     new_user = User (
#         name= 'Deepak',
#         email= 'dvshah13@gmail.com',
#         password= 'test123'
#         )
#     new_user.save()
#     print(new_user)
#
# # Create new user portfolio
# def add_user_portfolio():
#     new_portfolio = User_portfolio (
#         email= 'dvshah13@gmail.com',
#         stock_name= [apple, google]
#         )
#     new_portfolio.save()
#     print(new_portfolio)
# #
# def stock_filters():
#     posts = db.stock_filters
#     post_data = {
#         'Stock Name': 'apple',
#         'filters': 'various filters'
#     }
#     result = posts.insert_one(post_data)
#     print('One post: {0}'.format(result.inserted_id))

# Define what csv data to use
def define_stock_rsi(stock):
    # df = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl data/rsi_value.csv')
    # print list(df)
    if (stock == 'aapl'):
        my_stock = 'aapl data'
        read_stock_rsi(stock, my_stock)
    elif (stock == 'goog'):
        my_stock = 'goog data'
        read_stock_rsi(stock, my_stock)
    elif (stock == 'fb'):
        my_stock = 'fb data'
        read_stock_rsi(stock, my_stock)
    elif (stock == 'amzn'):
        my_stock = 'amzn data'
        read_stock_rsi(stock, my_stock)
    elif (stock == 'spy'):
        my_stock = 'spy data'
        read_stock_rsi(stock, my_stock)
    elif (stock == 'dis'):
        my_stock = 'dis data'
        read_stock_rsi(stock, my_stock)
    elif (stock == 'msft'):
        my_stock = 'msft data'
        read_stock_rsi(stock, my_stock)

# Read the rsi data for whichever stock is chosen
def read_stock_rsi(stock, my_stock):
    df_10da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ my_stock + '/rsi_value.csv', nrows=10)
    df_10da['RSI']
    rsi_values_10da = df_10da['RSI'].mean()
    df_20da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ my_stock + '/rsi_value.csv', nrows=20)
    df_20da['RSI']
    rsi_values_20da = df_20da['RSI'].mean()
    df_50da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ my_stock + '/rsi_value.csv', nrows=50)
    rsi_values_50da = df_50da['RSI'].mean()
    print stock, "RSI 10 day average: ", rsi_values_10da
    print stock, "RSI 20 day average: ", rsi_values_20da
    print stock, "RSI 50 day average: ", rsi_values_50da
    rsi_change_20_10 = (((rsi_values_10da / rsi_values_20da)-1) * 100)
    rsi_change_50_10 = (((rsi_values_10da / rsi_values_50da)-1) * 100)
    print "This is the RSI percentage change from 20 to 10 day: ", rsi_change_20_10
    print "This is the RSI percentage change from 50 to 10 day: ", rsi_change_50_10


##  Command list to test  ##
# add_user()
# add_user_portfolio()
# my_stock = 'alphabet'
# current_data(my_stock)
# current_data(stock)
# define_stock_rsi(stock)
