import random
import StringIO
from flask import Flask, make_response
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv
import pandas as pd
import datetime

# app = Flask(__name__)
#
# @app.route('/')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    # pd.read_csv('/app/daily_historical_prices/spy.csv', nrows=10)
    df = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/spy.csv', nrows=20)
    date_graph = pd.to_datetime(df['Date'])
    print date_graph
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

# if __name__ == '__main__':
#     app.run(debug=True)
