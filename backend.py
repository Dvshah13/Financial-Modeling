import csv
# import pandas as pd
from yahoo_finance import Share

sma_20day = []
rsi_20day = []

def current_data(stock):
    apple = Share(stock)
    print apple.get_price()
    print apple.get_volume()
    print apple.get_50day_moving_avg()
    print apple.get_percent_change_from_50_day_moving_average()
    print apple.get_price_earnings_ratio()
    print apple.get_price_earnings_growth_ratio()
    print apple.get_short_ratio()

current_data('AAPL')

# def get_data(filename):
# 	with open(filename, 'r') as csvfile:
# 		csvFileReader = csv.reader(csvfile)
# 		next(csvFileReader)	# skipping column names
# 		for row in csvFileReader:
# 			dates.append(int(row[0].split('-')[0]))
# 			rsi.append(float(row[1]))
