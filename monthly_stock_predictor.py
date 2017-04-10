import numpy
import csv
import urllib
from sklearn import *
from sklearn.metrics import *
# import matplotlib.pyplot as plt
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import *
from pybrain.datasets import *
from pybrain.structure.modules import *

def multiple_days_forward(data, days):
    labels = ((data[days:, 3] - data[days:, 0]) > 0).astype(int)
    data = data[:-days, :]
    return data, labels

### Heroku Routes ###
def stockData(symbol):
    data = list()
    if symbol == 'SPY':
        url = '/app/monthly_historical_prices/spy.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/spy.csv'  # local route
    elif symbol == 'AAPL':
        url = '/app/monthly_historical_prices/aapl.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/aapl.csv'  # local route
    elif symbol == 'GOOG':
        url = '/app/monthly_historical_prices/goog.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/goog.csv'  # local route
    elif symbol == 'FB':
        url = '/app/monthly_historical_prices/fb.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/fb.csv'  # local route
    elif symbol == 'AMZN':
        url = '/app/monthly_historical_prices/amzn.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/amzn.csv'  # local route
    elif symbol == 'DIS':
        url = '/app/monthly_historical_prices/dis.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/dis.csv'  # local route
    elif symbol == 'MSFT':
        url = '/app/monthly_historical_prices/msft.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/msft.csv'  # local route

    with open(url, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    data = numpy.array(data)
    data = data[1:, 1:]
    data = data.astype(float)
    labels = ((data[:, 3] - data[:, 0]) > 0).astype(int)
    data, labels = multiple_days_forward(data, 1)
    print numpy.shape(labels)
    print numpy.shape(data)

    def p_high(t, X):
        return max(X[:-t])

    def p_low(t, X):
        return min(X[:-t])

    def volume_high(t, X):
        return max(X[:-t])

    def volume_low(t, X):
        return min(X[:-t])

    def extract_features(data, indices):
        #remove the volume feature because of 0's
        data = data[:, [0, 1, 2, 3, 5]]
        #remove the first row because it is a header
        data2 = data[1:, :]
        features = data[:-1] - data2
        price_high = p_high(5, data[:, 1])
        price_low = p_low(5, data[:, 2])
        vol_high = volume_high(5, data[:, 4])
        vol_low = volume_low(5, data[:, 4])
        var1_diff_by_highlow = features[:, 0]/ float(price_high - price_low)
        var2_diff_by_highlow = features[:, 1]/float(price_high - price_low)
        mov_avg_by_data = list()
        for i in range(len(features)):
            mov_avg_by_data.append(numpy.mean(data[:i+1, :], axis = 0)/data[i, :])
        mov_avg_by_data = numpy.array(mov_avg_by_data)
        features = numpy.column_stack((features, var1_diff_by_highlow, var2_diff_by_highlow, mov_avg_by_data))
        print numpy.shape(features)
        return features[:, indices], data

    features, data = extract_features(data, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    train_features = features[:50]
    test_features = features[50:]
    train_labels = labels[:50]
    test_labels = labels[50:-1]

    clf = svm.SVC(kernel = 'rbf', C = 1.2, gamma = 0.001) # rbf kernel
    clf.fit(train_features, train_labels)

    predicted = clf.predict(test_features)
    predicted_svm = predicted[-1]
    if predicted_svm > 0:
        predicted_svm = "Positive"
    else:
        predicted_svm = "Negative"
    accuracy = accuracy_score(test_labels, predicted)
    precision = recall_score(test_labels, predicted)
    recall = precision_score(test_labels, predicted)
    print "Accuracy: ", accuracy
    print "Precision: ", precision
    print "Recall: ", recall
    data_algo_monthly = { 'SVM Accuracy': accuracy, 'SVM Precision': precision, 'SVM Recall': recall, 'Predicted SVM': predicted_svm }
    return data_algo_monthly

    # step = numpy.arange(0, len(test_labels))
    # plt.subplot(211)
    # plt.xlim(-1, len(test_labels) + 1)
    # plt.ylim(-1, 2)
    # plt.ylabel('Actual Values')
    # plt.plot(step, test_labels, drawstyle = 'step')
    # plt.subplot(212)
    # plt.xlim(-1, len(test_labels) + 1)
    # plt.ylim(-1, 2)
    # plt.xlabel('Months')
    # plt.ylabel('Predicted Values')
    # plt.plot(step, predicted, drawstyle = 'step')
    # plt.show()
