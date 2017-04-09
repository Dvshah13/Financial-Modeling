import numpy
import csv
import urllib
from sklearn import *
from sklearn.metrics import *
import matplotlib.pyplot as plt
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import *
from pybrain.datasets import *
from pybrain.structure.modules import *


def multiple_days_forward(data, days):
    labels = ((data[days:, 3] - data[days:, 0]) > 0).astype(int)
    data = data[:-days, :]
    return data, labels

# CSV Format: Date,Open,High,Low,Close,Volume,Adj Close
def stock_data(symbol):
    data = list()
    if symbol == 'SPY':
        url = '/app/daily_historical_prices/spy.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/spy.csv'  # local route
    elif symbol == 'AAPL':
        url = '/app/daily_historical_prices/aapl.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/aapl.csv'  # local route
    elif symbol == 'GOOG':
        url = '/app/daily_historical_prices/goog.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/goog.csv'  # local route
    elif symbol == 'FB':
        url = '/app/daily_historical_prices/fb.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/fb.csv'  # local route
    elif symbol == 'AMZN':
        url = '/app/daily_historical_prices/amzn.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/amzn.csv'  # local route
    elif symbol == 'DIS':
        url = '/app/daily_historical_prices/dis.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/dis.csv'  # local route
    elif symbol == 'MSFT':
        url = '/app/daily_historical_prices/msft.csv'  # Heroku route
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/daily_historical_prices/msft.csv'  # local route

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

    # Feature Extraction
    def extract_features(data, indices):
        data = data[:, [0, 1, 2, 3, 5]]
        # remove the first row because it is a header
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

    features, data = extract_features(data, [0, 1, 2, 3, 4])
    train_features = features[:1000]
    test_features = features[1000:]
    train_labels = labels[:1000]
    test_labels = labels[1000:-1]

    clf = svm.SVC(kernel = 'rbf', C = 1.2, gamma = 0.001)  # rbf kernel
    clf.fit(train_features, train_labels)

    predicted = clf.predict(test_features)
    predicted_svm = predicted[-1]
    if predicted_svm > 0:
        predicted_svm = "Positive"
    else:
        predicted_svm = "Negative"
    accuracy_svm = accuracy_score(test_labels, predicted)
    precision_svm = recall_score(test_labels, predicted)
    recall_svm = precision_score(test_labels, predicted)
    print "Accuracy: ", accuracy_svm
    print "Precision: ", precision_svm
    print "Recall: ", recall_svm

## RNN
    net = buildNetwork(5, 20, 1, hiddenclass = LSTMLayer, outclass = SigmoidLayer, recurrent = True)
    ds = ClassificationDataSet(5, 1)
    for i, j in zip(train_features, train_labels):
        ds.addSample(i, j)

    trainer = BackpropTrainer(net, ds)

    epochs = 10
    for i in range(epochs):
        trainer.train()

    predicted = list()
    for i in test_features:
        predicted.append(int(net.activate(i)>0.5))
    predicted = numpy.array(predicted)

    predicted_rnn = predicted[-1]
    if predicted_rnn > 0:
        predicted_rnn = "Positive"
    else:
        predicted_rnn = "Negative"
    accuracy_rnn = accuracy_score(test_labels, predicted)
    recall_rnn = recall_score(test_labels, predicted)
    precision_rnn = precision_score(test_labels, predicted)
    print "Accuracy: ", accuracy_score(test_labels, predicted)
    print "Recall: ", recall_score(test_labels, predicted)
    print "Precision: ", precision_score(test_labels, predicted)
    data_algo_daily = { 'SVM Accuracy': accuracy_svm, 'SVM Precision': precision_svm, 'SVM Recall': recall_svm, 'Predicted SVM': predicted_svm, 'RNN Accuracy': accuracy_rnn, 'RNN Precision': precision_rnn, 'RNN Recall': recall_rnn, 'Predicted RNN': predicted_rnn }
    return data_algo_daily
