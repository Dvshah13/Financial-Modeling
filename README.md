# DMR Capital
Financial Data Modeling using Machine Learning

<b>Link to live site:</b> <a href='https://financial-modeling-dmr.herokuapp.com/'>DMR Capital</a><br>
To Test: <br>
Username - test@123.com<br>
Password - Test123<br><br>
<b>Programmer and Designer:</b> <br>
Deepak Shah 
![alt tag](https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_capital_fp.png?raw=true)

<b>Technologies, Frameworks and Programming Languages:</b><br>
Python, Numpy, Pandas, PyBrain, Scipy, Scikit Learn, Flask, MongoDb, Javascript, jQuery, HTML, CSS, Heroku
<br><br>
<b>Overview of Project:</b><br>
DMR Capital was built to allow users to utilize machine learning systems (Support Vector Machine and Recurrent Neural Net), sentiment analysis and basic stock data and indicators to make informed trading decisions to generate above average market return. 
<br><br>
<b>My Process/Technical Bits Summarized:</b><br>
When starting this project, I knew I wanted to explore the relationship between machine learning and predicitive modeling in the stock market but knew there would be some interesting and fun challenges ahead since markets could have a potentially complex list of features, I would be using time series data (had to plan accordingly as to normalize or rescale aka transform to improve performance) and the random walk theory that many believe drive markets, which states that the past movement or direction of the price of a stock or overall market cannot be used to predict its future movement.  <br><br>
I'd like to take you through my general process that I use as I start most of my machine learning projects, my guidebook if you will.  Identify what I'm doing: I want to build a predictive model to determine future price action in the stock market.  Now I have a target, next up the most important aspect of any project: Data, oh data... data collection, preparation, processing, cleaning this is the most important part of your project and getting this step right can make or break your model.  In the stock market, there are a multitude of factors that people believe drive future stock prices.  I knew that I had to be careful to pick the right features and that meant spending a lot of time understanding the data and justify why each feature selected was an important feature to add.  With my background in finance, I thought I had a resonable idea of what I wanted to use but I then had to put on my data science hat on and look whether the features chosen had multicollinearity (features that are highly correlated).  This part may be time consuming but it is crucial to get what you aim for, an accurate and robust model.  I ended up going with price, volume and moving averages which is a strategy I employed as a trader and stored that for each stock as a CSV.  <br><br>
Next up, model selection, in general you want to start with the simplest model and only add complexity if another model performs better.  This was a lesson I learned when I initially started data science projects.  I was so excited about the complex models, neural nets with backprop or boosted decision trees and they may end up being great models for your data but many times you are adding complexity just for the sake of it when something like linear/logistic regression might just do the trick for the data your are modeling.  With that said, I looked at logistic regression first since I was making a binary classification (up/down, 1/0 respectively).  Even with some modest tuning, my predictive accuracy, precision and recall was not what I had hoped (roughly 55-60% respectively).  Next I went with a kernel SVM, given using a kernel, I expected the model to do better with the data.  I ended up using the 'RBF', radial basis function kernel which has been shown to do well with classification and upon testing, got accuracies closer to 85-89%, precision and recall at levels that were acceptable as well (85%+).  Note, accuracy is not the end all be all of validating performance of a model.  Recall (relevency or true positives were recalled) represented by the formula, TP/(TP + FN) and precision (what was recalled was a true positive) represented by TP/(TP+FP), where TP = true positive, FN = false negative and FP = false positive.  Given the time constraints I stopped there and moved on to building the neural network with backprop.  In the future, I'd like to try some different methods, I've read how random forests have been promising in this task.  <br><br>
So on to the neural network with backprop, here my choice was a bit simpler.  I decided to go with the RNN specifically the LSTM.  My reasoning was the LSTM can typically handle time series and sequential data which the stock market is based on very well.  The RNN has some internal memory of what it saw previously and that would be very useful for data such as stock prices.  It uses that memory to decide how exactly it should operate on the next input. Thus an RNN remembers within the scope and for predictive modeling especially the stock market where momentum weighs heavily it would be nice to treat events as related and not just forget.  With some slight tuning to the epochs and choosing a sigmoid activation function, the model performed well enough in accuracy, precision and recall for me to accept the results.   <br><br>
I also wanted to add sentiment analysis as sentiment is one of the most difficult things to measure in the market.  It can play a huge role in stock movement but it largely hard to pinpoint.  I started using twitter as a medium for voices on the market to be heard and analyzed.  Using twitter's api and textblob, I was able to parse through an indivdual companies stock mentions and look at each stocks polarity and subjectivity.  By having these features, I attempted to categorize whether a response was positive or negative towards the equity and present this to the user.
<br><br>
<b>Features:</b>
<li>Utilize Support Vector Machine (SVM) and Recurrent Neural Net (RNN) predicitive analysis to forecast future moves.</li>
<li>Delivers sentiment analysis through twitter and sorted by positive and negative sentiment and filtered by polarity and subjectivity.</li>
<li>On your dashboard have access to all the pertinant information you need to make informed and profitable decisions.</li>

![alt tag](https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen1.png?raw=true)


<br><br>
<b>Screenshots</b><br><br>
<b>SVM Classifier Code</b><br>
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen2.png?raw=true" height="250">
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen3.png?raw=true" height="60">
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen4.png?raw=true" height="120">
<br><b>RNN Code</b><br>
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen5.png?raw=true" height="250">
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen6.png?raw=true" height="150">
<br><b>Twitter Sentiment Analysis</b><br>
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen7.png?raw=true" height="250">
<br><b>Predicted Array and Actual Array</b><br>
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen_console.png?raw=true" height="250">
<br><b>MathPlotLib Graph</b><br>
<img src="https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/mathplotlib.png?raw=true" height="250">
