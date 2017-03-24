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




def multiple_days_forward(data, days):
    labels = ((data[days:, 3] - data[days:, 0]) > 0).astype(int)
    data = data[:-days, :]
    return data, labels


### Heroku Routes ###

def stockData(symbol):
    data = list()
    if symbol == 'SPY':
        url = '/app/weekly_historical_prices/spy.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/spy.csv'  # local route
    elif symbol == 'AAPL':
        url = '/app/weekly_historical_prices/aapl.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/aapl.csv'  # local route
    elif symbol == 'GOOG':
        url = '/app/weekly_historical_prices/goog.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/goog.csv'  # local route
    elif symbol == 'FB':
        url = '/app/weekly_historical_prices/fb.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/fb.csv'  # local route
    elif symbol == 'AMZN':
        url = '/app/weekly_historical_prices/amzn.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/amzn.csv'  # local route
    elif symbol == 'DIS':
        url = '/app/weekly_historical_prices/dis.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/dis.csv'  # local route
    elif symbol == 'MSFT':
        url = '/app/weekly_historical_prices/msft.csv'  # Heroku Routes
        # url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/weekly_historical_prices/msft.csv'  # local route

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
    train_features = features[:200]
    test_features = features[200:]
    train_labels = labels[:200]
    test_labels = labels[200:-1]


    # In[163]:

    clf = svm.SVC(kernel = 'rbf', C = 1.2, gamma = 0.001)
    clf.fit(train_features, train_labels)


    # In[164]:

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


    net = buildNetwork(12, 20, 1, hiddenclass = LSTMLayer, outclass = SigmoidLayer, recurrent = True)
    ds = ClassificationDataSet(12, 1)
    for i, j in zip(train_features, train_labels):
        ds.addSample(i, j)


    # In[168]:

    trainer = BackpropTrainer(net, ds)


    # In[169]:

    epochs = 100
    for i in range(epochs):
        trainer.train()


    # In[170]:

    predicted = list()
    for i in test_features:
        #print net.activate(i)
        predicted.append(int(net.activate(i)>0.5))
    predicted = numpy.array(predicted)


    # In[171]:
    predicted_rnn = predicted[-1]
    if predicted_rnn > 0:
        predicted_rnn = "Positive"
    else:
        predicted_rnn = "Negative"
    accuracy_rnn = accuracy_score(test_labels, predicted)
    recall_rnn = recall_score(test_labels, predicted)
    precision_rnn = precision_score(test_labels, predicted)
    print accuracy_score(test_labels, predicted)
    print recall_score(test_labels, predicted)
    print precision_score(test_labels, predicted)
    data_algo_weekly = { 'SVM Accuracy': accuracy_svm, 'SVM Precision': precision_svm, 'SVM Recall': recall_svm, 'Predicted SVM': predicted_svm, 'RNN Accuracy': accuracy_rnn, 'RNN Precision': precision_rnn, 'RNN Recall': recall_rnn, 'Predicted RNN': predicted_rnn }
    return data_algo_weekly

# In[165]:

    # # In[166]:
    #
    # step = numpy.arange(0, len(test_labels))
    # plt.subplot(211)
    # plt.xlim(-1, len(test_labels) + 1)
    # plt.ylim(-1, 2)
    # plt.ylabel('Actual Values')
    # plt.plot(step, test_labels, drawstyle = 'step')
    # plt.subplot(212)
    # plt.xlim(-1, len(test_labels) + 1)
    # plt.ylim(-1, 2)
    # plt.xlabel('Weeks')
    # plt.ylabel('Predicted Values')
    # plt.plot(step, predicted, drawstyle = 'step')
    # plt.show()
