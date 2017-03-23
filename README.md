# DMR Capital
Financial Data Modeling using Machine Learning

<b>Link to live site:</b> <a href='https://financial-modeling-dmr.herokuapp.com/'>DMR Capital</a><br><br>
<b>Programmer and Designer:</b> <br>
Deepak Shah 
![alt tag](https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_capital_fp.png?raw=true)

<b>Technologies, Frameworks and Programming Languages:</b><br>
Python, Numpy, Pandas, PyBrain, Scipy, Scikit Learn, Flask, MongoDb, Javascript, jQuery, HTML, Sass CSS, Heroku
<br><br>
<b>Technology Details:</b><br>
When starting the project, I knew I wanted to explore the relationship between machine learning and predicitive modeling as they are a natural fit.  I was intrigued with deep learning to see if the results might be enhanced by having both something with back propagation.  I had read about the success that classifiers had with data such as the stock market so that was the first avenue I decided to persue.  I was deciding between logistic regression, decision trees and SVM.  Logistic regression would certainly be easier to scale and build but it's simplicity seemed to also be a hinderance in something as complex as the stock market.  Creating a decision boundry and making classifications would imo lead to weak correlation.  Decision trees were the next logical step but although it was capable of handling more complexity I was afraid of running the risk of overfitting and its strong bias which may yield good results in training but fail in testing.  I ended up going with SVMs because considering the large number of features and number of observations it would be a bit more accurate in this case and not overly bias towards the training data.  Next I decided I wanted to test out how well a neural network could compete with a classifier and I decided to go with the RNN.  My reasoning was RNNs typically handle time series and sequential data which the stock market is based on.  In this sense the RNN has some internal memory of what it saw previously. It uses that memory to decide how exactly it should operate on the next input. Thus an RNN remembers within the scope and for predictive modeling especially the stock market where momentum weighs heavily it would be essential to treat events as related and not just forget.
<br><br>
<b>Overview of Project:</b><br>
DMR Capital was built to allow users to utilize machine learning systems (Support Vector Machine and Recurrent Neural Net), sentiment analysis and basic stock data and indicators to make informed trading decisions to generate above average market return. 


<b>Features:</b>
<li>Utilize Support Vector Machine (SVM) and Recurrent Neural Net (RNN) predicitive analysis to forecast future moves.</li>
<li>Delivers sentiment analysis through twitter and sorted by positive and negative sentiment and filtered by polarity and subjectivity.</li>
<li>On your dashboard have access to all the pertinant information you need to make informed and profitable decisions.</li>

![alt tag](https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_screen1.png?raw=true)


<br><br>
<b>Screenshots and Explanations</b><br>
