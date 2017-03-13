import csv
# import pandas as pd
from yahoo_finance import Share

sma_20day = []
rsi_20day = []

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

my_stock = 'apple'
current_data(my_stock)

# def get_data(filename):
# 	with open(filename, 'r') as csvfile:
# 		csvFileReader = csv.reader(csvfile)
# 		next(csvFileReader)	# skipping column names
# 		for row in csvFileReader:
# 			dates.append(int(row[0].split('-')[0]))
# 			rsi.append(float(row[1]))
