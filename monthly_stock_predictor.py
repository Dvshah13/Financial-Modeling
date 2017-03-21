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
#%matplotlib inline


# In[132]:

def multiple_days_forward(data, days):
    labels = ((data[days:, 3] - data[days:, 0]) > 0).astype(int)
    data = data[:-days, :]
    return data, labels


# In[155]:

# data = list()
# print "Enter Company/Stock: "
# print "1. SPY"
# print "2. AAPL"
# print "3. GOOG"
# print "4. FB"
# print "5. AMZN"
# print "6. DIS"
# print "7. MSFT"
# case = int(input())


# In[156]:
def stockData(symbol):
    data = list()
    if symbol == 'SPY':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/spy.csv'
    elif symbol == 'AAPL':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/aapl.csv'
    elif symbol == 'GOOG':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/goog.csv'
    elif symbol == 'FB':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/fb.csv'
    elif symbol == 'AMZN':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/amzn.csv'
    elif symbol == 'DIS':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/dis.csv'
    elif symbol == 'MSFT':
        url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/monthly_historical_prices/msft.csv'

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


    # In[157]:

    def t_high(t, X):
        return max(X[:-t])


    # In[158]:

    def t_low(t, X):
        return min(X[:-t])


    # In[159]:

    def volume_high(t, X):
        return max(X[:-t])


    # In[160]:

    def volume_low(t, X):
        return min(X[:-t])


    # In[161]:

    def extract_features(data, indices):
        #remove the volume feature because of 0's
        data = data[:, [0, 1, 2, 3, 5]]
        #remove the first row because it is a header
        data2 = data[1:, :]
        features = data[:-1] - data2
        Phigh = t_high(5, data[:, 1])
        Plow = t_low(5, data[:, 2])
        vhigh = volume_high(5, data[:, 4])
        vlow = volume_low(5, data[:, 4])
        Odiff_by_highlow = features[:, 0]/ float(Phigh - Plow)
        Cdiff_by_highlow = features[:, 1]/float(Phigh - Plow)
        mov_avg_by_data = list()
        for i in range(len(features)):
            mov_avg_by_data.append(numpy.mean(data[:i+1, :], axis = 0)/data[i, :])
        mov_avg_by_data = numpy.array(mov_avg_by_data)
        features = numpy.column_stack((features, Odiff_by_highlow, Cdiff_by_highlow, mov_avg_by_data))
        print numpy.shape(features)
        return features[:, indices], data


    # In[162]:

    features, data = extract_features(data, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    train_features = features[:50]
    test_features = features[50:]
    train_labels = labels[:50]
    test_labels = labels[50:-1]


    # In[163]:

    clf = svm.SVC(kernel = 'rbf', C = 1.2, gamma = 0.001)
    clf.fit(train_features, train_labels)


    # In[164]:

    predicted = clf.predict(test_features)
    accuracy = accuracy_score(test_labels, predicted)
    precision = recall_score(test_labels, predicted)
    recall = precision_score(test_labels, predicted)
    print "Accuracy: ", accuracy
    print "Precision: ", precision
    print "Recall: ", recall
    data_algo_monthly = { 'SVM Accuracy': accuracy, 'SVM Precision': precision, 'SVM Recall': recall }
    return data_algo_monthly


    # In[165]:
    #
    # bought_price = list()
    # current_holdings = 0
    # sell_price = list()
    # for i in range(len(predicted)):
    #     if predicted[i]:
    #         current_holdings += 1
    #         bought_price.append(data[50+(i+1), 0])
    #     else:
    #         for j in range(current_holdings):
    #             sell_price.append(data[50+(i+1), 0])
    #         current_holdings = 0
    # print sum(sell_price) - sum(bought_price)
    #
    #
    # # In[166]:

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
