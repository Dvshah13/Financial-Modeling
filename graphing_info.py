import random
import StringIO
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv
import pandas as pd
import datetime

def stock_data(symbol):
    if symbol == 'SPY':
        # url = '/app/daily_historical_prices/spy.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/spy.csv'  # local route
    elif symbol == 'AAPL':
        # url = '/app/daily_historical_prices/aapl.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/aapl.csv'  # local route
    elif symbol == 'GOOG':
        # url = '/app/daily_historical_prices/goog.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/goog.csv'  # local route
    elif symbol == 'FB':
        # url = '/app/daily_historical_prices/fb.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/fb.csv'  # local route
    elif symbol == 'AMZN':
        # url = '/app/daily_historical_prices/amzn.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/amzn.csv'  # local route
    elif symbol == 'DIS':
        # url = '/app/daily_historical_prices/dis.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/dis.csv'  # local route
    elif symbol == 'MSFT':
        # url = '/app/daily_historical_prices/msft.csv'  # Heroku route
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/msft.csv'  # local route


    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    # pd.read_csv('/app/daily_historical_prices/spy.csv', nrows=10)
    df = pd.read_csv(url, nrows=30)
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
