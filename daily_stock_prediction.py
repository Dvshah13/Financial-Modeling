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
#%matplotlib inline


# In[ ]:

def multiple_days_forward(data, days):
    labels = ((data[days:, 3] - data[days:, 0]) > 0).astype(int)
    data = data[:-days, :]
    return data, labels


# In[ ]:

data = list()
print "Enter Company/Stock: "
print "1. SPY"
print "2. AAPL"
print "3. GOOG"
print "4. FB"
print "5. AMZN"
print "6. DIS"
case = int(input())


# In[ ]:

# CSV Format: Date,Open,High,Low,Close,Volume,Adj Close

if case == 1:
    url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/spy.csv'
elif case == 2:
    url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/aapl.csv'
elif case == 3:
    url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/goog.csv'
elif case == 4:
    url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/fb.csv'
elif case == 5:
    url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/amzn.csv'
elif case == 6:
    url = '/Users/deepakshah/Documents/Digital Crafts/Machine Learning/Financial Modeling/dis.csv'

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


# In[ ]:

def t_high(t, X):
    return max(X[:-t])


# In[ ]:

def t_low(t, X):
    return min(X[:-t])


# In[ ]:

def volume_high(t, X):
    return max(X[:-t])


# In[ ]:

def volume_low(t, X):
    return min(X[:-t])


# In[ ]:

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


# In[ ]:

features, data = extract_features(data, [0, 1, 2, 3, 4])
train_features = features[:1000]
test_features = features[1000:]
train_labels = labels[:1000]
test_labels = labels[1000:-1]


# In[ ]:

clf = svm.SVC(kernel = 'rbf', C = 1.2, gamma = 0.001)
clf.fit(train_features, train_labels)


# In[ ]:

predicted = clf.predict(test_features)
Accuracy = accuracy_score(test_labels, predicted)
Precision = recall_score(test_labels, predicted)
Recall = precision_score(test_labels, predicted)
print "Accuracy: ", Accuracy
print "Precision: ", Precision
print "Recall: ", Recall


# In[ ]:

step = numpy.arange(0, len(test_labels))
plt.subplot(211)
plt.xlim(-1, len(test_labels) + 1)
plt.ylim(-1, 2)
plt.ylabel('Actual Values')
plt.plot(step, test_labels, drawstyle = 'step')
plt.subplot(212)
plt.xlim(-1, len(test_labels) + 1)
plt.ylim(-1, 2)
plt.xlabel('Days')
plt.ylabel('Predicted Values')
plt.plot(step, predicted, drawstyle = 'step')
plt.show()
#plt.plot(plot_predicted)


# In[ ]:

#net = RecurrentNetwork()
#net.addInputModule(LinearLayer(3, name = 'in'))
#net.addInputModule(SigmoidLayer(4, name = 'hidden'))
#net.addOutputModule(LinearLayer(1, name = 'output'))
#net.addConnection(FullConnection(net['in'], net['hidden'], name = 'c1'))
#net.addConnection(FullConnection(net['hidden'], net['output'], name = 'c2'))
#net.addRecurrentConnection(FullConnection(net['hidden'], net['hidden'], name='c3'))
net = buildNetwork(5, 20, 1, hiddenclass = LSTMLayer, outclass = SigmoidLayer, recurrent = True)
ds = ClassificationDataSet(5, 1)
for i, j in zip(train_features, train_labels):
    ds.addSample(i, j)


# In[ ]:

trainer = BackpropTrainer(net, ds)


# In[ ]:

epochs = 10
for i in range(epochs):
    trainer.train()


# In[ ]:

predicted = list()
for i in test_features:
    #print net.activate(i)
    predicted.append(int(net.activate(i)>0.5))
predicted = numpy.array(predicted)


# In[ ]:

print "Accuracy: ", accuracy_score(test_labels, predicted)
print "Recall: ", recall_score(test_labels, predicted)
print "Precision: ", precision_score(test_labels, predicted)


# In[ ]:

step = numpy.arange(0, len(test_labels))
plt.subplot(211)
plt.xlim(-1, len(test_labels) + 1)
plt.ylim(-1, 2)
plt.plot(step, test_labels, drawstyle = 'step')
plt.ylabel('Actual Values')
plt.subplot(212)
plt.xlim(-1, len(test_labels) + 1)
plt.ylim(-1, 2)
plt.plot(step, predicted, drawstyle = 'step')
plt.xlabel('Days')
plt.ylabel('Predicted Values')
plt.show()
#plt.plot(plot_predicted)


# In[ ]:
