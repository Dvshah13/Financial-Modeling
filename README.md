# DMR Capital
Financial Data Modeling using Machine Learning

<b>Link to live site:</b> <a href='https://financial-modeling-dmr.herokuapp.com/'>DMR Capital</a><br><br>
<b>Contributors:</b> <br>
Deepak Shah 
<br><br>
<b>Technologies, Frameworks and Programming Languages:</b><br>
Python, Numpy, Pandas, PyBrain, Scipy, Scikit Learn, Flask, MongoDb, Javascript, jQuery, HTML, Sass CSS, Heroku
<br><br><b>Overview of Project:</b><br>
DMR Capital was built to allow users to utilize machine learning systems, sentiment analysis and basic stock data and indicators to make informed trading decisions to generate above average market return. 
![alt tag](https://github.com/Dvshah13/Screens-for-Data-Science-Projects/blob/master/dmr_capital_fp.png?raw=true)
<b>Features:</b>
<li>Utilize Support Vector Machine (SVM) and Recurrent Neural Net (RNN) predicitive analysis to forecast future moves.</li>
<li>Delivers sentiment analysis through twitter and sorted by positive and negative sentiment and filtered by polarity and subjectivity.</li>
<li>On your dashboard have access to all the pertinant information you need to make informed and profitable decisions.</li>
<br>

***

<b>Challenges faced & Solutions used:</b>
<br>1. One of the earliest challenges the team faced how to design each socket so that we could construct a new socket to handle a new document and not disturb the other socket connections. The solution we implemented was assign by id a new room with socket connection and then new documents were created for them to be assigned new sockets.  Thus any room now had an id attachment to reference.<br>
<img src="https://github.com/Dvshah13/markWith-Screens/blob/master/CS1.png?raw=true" height="250">

<br>2. The next challenge we faced involved the logistics between rendering the content live and saving upon keystroke to our data base so that content was updated real time but also saved so it could be accessed anytime a user logged in.  We also needed to make sure the most current updated document was broadcast to each user.  The solution here was two-fold, first we saved after every keystroke by overwriting the current content which allowed for live rendering and dynamic save points. And we also passed in the document id so the content knew where it need to broadcast.<br>
<img src="https://github.com/Dvshah13/markWith-Screens/blob/master/CS2.png?raw=true" height="250">

<br>3. Another challenged we faced involved authentication at multiple stages.  Authentication was necessary as both a user and a document as permission levels dictated what features were allowed.  The user authenticity we wanted to implement was a cookie based session so users could sign in and stay active without having to re-login at every close.
<br>
<img src="https://github.com/Dvshah13/markWith-Screens/blob/master/CS3.png?raw=true" height="250">


<br>4. Document authentication was also a major challenge because document owners were granted privledges not available to document collaborators and we need a system to verify authentication level and not allow either side to have access they were not allowed to have.  The solution we chose to implement here was to define an owner and collaborator at each doucment stage and run that on the api.  We would check against the database and once defined, the access and privledges were granted were necessary.
<br>
<img src="https://github.com/Dvshah13/markWith-Screens/blob/master/CS4.png?raw=true" height="250">

***

<br><b>Error handling/Troubleshooting:</b></br>
Given the back end intensive nature of our project and async issues that could arise, we faced our fair share of delicate troubleshooting issues which we eventually worked out and wanted to share what we learned from each issue.
<br>
<br>1. Just in general given that there could be a potential error at every stage of the process, we had to have fail-safes to handle any of those issues.  On the document side, we had to deal with async issues and then have callbacks that would spit out errors as necessary.  An example of this is as follows: <br>
<img src="https://github.com/Dvshah13/markWith-Screens/blob/master/EH1.png?raw=true" height="250">

<br>2. On the user side, we used a lot of nested conditionals to verify and error handle.  It was done very similarly to the document code shown above (callbacks to keep sync issues in check).  Here is an example of updating a user, using nested conditionals to check at each stage.<br>
<img src="https://github.com/Dvshah13/markWith-Screens/blob/master/EH1.png?raw=true" height="250">

***

<b>MVP and Stretch Goals:</b>
<br>
<br><b>MVP (Minimum Viable Product)</b><br>
<li>Build a markdown editor, that could be accessed by multiple users at the same time.</li>
<li>Allow for live editing and a dynamically generated output.</li>
<li>Store content and document information so it can be accessed by users later on.</li>
<br><b>Stetch Goals</b><br>
<li>Add a demo to landing page so users can test markWith before signing up.</li>
<li>Build a documents store so documents can be rendered and accessed easily by users.</li>
<li>Add more mobile responsive features</li>
<b><br>Contribution we'd like to be added:</b><br>
<li>Invite system so collaborators can be informed they've been added to a document.</li>
<li>Chat room in each document so collaborators can communicate with each other.</li>


