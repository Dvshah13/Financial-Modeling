import csv
import pandas as pd

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
def read_stock_rsi(symbol):
    df_10da = pd.read_csv('/app/'+ symbol.lower()+' data' + '/rsi_value.csv', nrows=10)  # Heroku Routes
    # df_10da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ symbol.lower()+' data' + '/rsi_value.csv', nrows=10)  # Local Routes
    df_10da['RSI']
    rsi_values_10da = df_10da['RSI'].mean()
    df_20da = pd.read_csv('/app/'+ symbol.lower()+' data' + '/rsi_value.csv', nrows=20)  # Heroku Routes
    # df_20da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ symbol.lower()+' data' + '/rsi_value.csv', nrows=20)  # Local Routes
    df_20da['RSI']
    rsi_values_20da = df_20da['RSI'].mean()
    df_50da = pd.read_csv('/app/'+ symbol.lower()+' data' + '/rsi_value.csv', nrows=50)  # Heroku Routes
    # df_50da = pd.read_csv('/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/'+ symbol.lower()+' data' + '/rsi_value.csv', nrows=50)  # Local Routes
    rsi_values_50da = df_50da['RSI'].mean()
    print rsi_values_10da
    print "Worked"
    rsi_values_10_mean = rsi_values_10da
    rsi_values_20_mean = rsi_values_20da
    rsi_values_50_mean = rsi_values_50da
    rsi_change_20_10 = (((rsi_values_10_mean / rsi_values_20_mean)-1) * 100)
    rsi_change_50_10 = (((rsi_values_10_mean / rsi_values_50_mean)-1) * 100)
    data_set2 = {'RSI 10 Day Average':rsi_values_10_mean, 'RSI 20 Day Average':rsi_values_20_mean, 'RSI 50 Day Average':rsi_values_50_mean, 'RSI Percent Change 10 to 20 Day':rsi_change_20_10, 'RSI Percent Change 10 to 50 Day':rsi_change_50_10 }
    return data_set2
