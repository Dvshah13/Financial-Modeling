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
    if stock == 'apple':
        stock = Share('AAPL')
        data_front_page(stock)

    elif stock == 'alphabet':
        stock = Share('GOOG')
        data_front_page(stock)

def data_front_page(stock):
    print stock.get_price()
    print stock.get_percent_change()
    print stock.get_volume()
    print stock.get_ebitda()
    print stock.get_50day_moving_avg()
    print stock.get_percent_change_from_50_day_moving_average()
    print stock.get_price_earnings_ratio()
    print stock.get_price_earnings_growth_ratio()
    print stock.get_short_ratio()

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

# Read excel/csv data
def read_stock_rsi():
    # df = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl data/rsi_value.csv')
    # print list(df)
    df_10da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl data/rsi_value.csv', nrows=10)
    df_10da['RSI']
    rsi_values_10da = df_10da['RSI'].mean()
    df_20da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl data/rsi_value.csv', nrows=20)
    df_20da['RSI']
    rsi_values_20da = df_20da['RSI'].mean()
    df_50da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl data/rsi_value.csv', nrows=50)
    rsi_values_50da = df_50da['RSI'].mean()
    print rsi_values_10da
    print rsi_values_20da
    print rsi_values_50da
    rsi_change_20_10 = (((rsi_values_10da / rsi_values_20da)-1) * 100)
    rsi_change_50_10 = (((rsi_values_10da / rsi_values_50da)-1) * 100)
    print rsi_change_20_10
    print rsi_change_50_10

# add_user()
# add_user_portfolio()
my_stock = 'alphabet'
current_data(my_stock)
# read_stock_rsi()
