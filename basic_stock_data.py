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
    if stock == 'AAPL':
        symbol = Share('AAPL')
        data_front_page(symbol)
    elif stock == 'GOOG':
        symbol = Share('GOOG')
        data_front_page(symbol)
    elif stock == 'SPY':
        symbol = Share('SPY')
        data_front_page(symbol)
    elif stock == 'FB':
        symbol = Share('FB')
        data_front_page(symbol)
    elif stock == 'AMZN':
        symbol = Share('AMZN')
        data_front_page(symbol)
    elif stock == 'DIS':
        symbol = Share('DIS')
        data_front_page(symbol)
    elif stock == 'MSFT':
        symbol = Share('MSFT')
        data_front_page(stock, symbol)

def data_front_page(symbol):
    current_price = Share(symbol).get_price()
    per_change = Share(symbol).get_percent_change()
    curr_volume = Share(symbol).get_volume()
    ebitda = Share(symbol).get_ebitda()
    curr_50day = Share(symbol).get_50day_moving_avg()
    curr_perchan_50 = Share(symbol).get_percent_change_from_50_day_moving_average()
    pe_ratio = Share(symbol).get_price_earnings_ratio()
    peg_ratio = Share(symbol).get_price_earnings_growth_ratio()
    short_ratio = Share(symbol).get_short_ratio()
    earnings_estimate_next_quarter = Share(symbol).get_EPS_estimate_next_quarter()
    earnings_estimate_next_year = Share(symbol).get_price_EPS_estimate_next_year()
    year_range = Share(symbol).get_year_range()
    per_chan_high = Share(symbol).get_percent_change_from_year_high()
    per_chan_low = Share(symbol).get_percent_change_from_year_low()
    one_year_price_target = Share(symbol).get_one_yr_target_price()
    data_set1 = {'Current Price':current_price, 'Daily Percent Change':per_change, 'Daily Volume':curr_volume, 'EBITDA':ebitda, 'Current 50 Day SMA':curr_50day, '% Change from 50 Day SMA':curr_perchan_50, 'PE Ratio':pe_ratio, 'PEG Ratio':peg_ratio, 'Shares Short Ratio':short_ratio, 'Earnings Est Next Quarter': earnings_estimate_next_quarter, 'Earnings Est Next Year': earnings_estimate_next_year, 'Year Range': year_range, 'Year Range % Change From High': per_chan_high, 'Year Range % Change From Low': per_chan_low, 'One Year Price Target': one_year_price_target }
    return data_set1

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

def define_stock_rsi(symbol):
    # df = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl data/rsi_value.csv')
    # print list(df)
    if (symbol == 'AAPL'):
        my_stock = 'aapl data'
        read_stock_rsi(my_stock)
    elif (symbol == 'GOOG'):
        my_stock = 'goog data'
        read_stock_rsi(my_stock)
    elif (symbol == 'FB'):
        my_stock = 'fb data'
        read_stock_rsi(my_stock)
    elif (symbol == 'AMZN'):
        my_stock = 'amzn data'
        read_stock_rsi(my_stock)
    elif (symbol == 'SPY'):
        my_stock = 'spy data'
        read_stock_rsi(my_stock)
    elif (symbol == 'DIS'):
        my_stock = 'dis data'
        read_stock_rsi(my_stock)
    elif (symbol == 'MSFT'):
        my_stock = 'msft data'
        read_stock_rsi(my_stock)

# Read the rsi data for whichever stock is chosen
def read_stock_rsi(my_stock):
    df_10da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ my_stock + '/rsi_value.csv', nrows=10)
    df_10da['RSI']
    rsi_values_10da = df_10da['RSI'].mean()
    df_20da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ my_stock + '/rsi_value.csv', nrows=20)
    df_20da['RSI']
    rsi_values_20da = df_20da['RSI'].mean()
    df_50da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ my_stock + '/rsi_value.csv', nrows=50)
    rsi_values_50da = df_50da['RSI'].mean()
    print rsi_values_10da
    print "Worked"
    rsi_values_10_mean = rsi_values_10da
    rsi_values_20_mean = rsi_values_20da
    rsi_values_50_mean = rsi_values_50da
    rsi_change_20_10 = (((rsi_values_10_mean / rsi_values_20_mean)-1) * 100)
    rsi_change_50_10 = (((rsi_values_10_mean / rsi_values_50_mean)-1) * 100)
    data_set2 = {'rsi_values_10_mean':rsi_values_10_mean, 'rsi_values_20_mean':rsi_values_20_mean, 'rsi_values_50_mean':rsi_values_50_mean, 'rsi_change_20_10':rsi_change_20_10, 'rsi_change_50_10':rsi_change_50_10 }
    return data_set2
    # print data_set2['rsi_change_50_10']

##  Command list to test  ##
# add_user()
# add_user_portfolio()
# my_stock = 'alphabet'
# current_data(my_stock)
# current_data(stock)
# define_stock_rsi(symbol)
