import tweepy
from textblob import TextBlob

# Authenticate twitter api
consumer_key= 'mKYCldV2UPdskRZGfEWXg4HVj'
consumer_secret= '9QbLwAszCylsaWvW66niS3VMQd64yA7OI10814xeejr6S9fTrz'

access_token='30805254-rxQUZ8C8eFwBpUnn4dJFSM1mg5njEhC0QoGZepEZm'
access_token_secret='v3yHjW1fJElSbcCutbfMpk571J1pw8mfAzb9ydOkLnD3k'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Define positive and negative tweets


# Retrieve Tweets
def findStock(symbol):
    if symbol == 'AAPL':
        public_tweets = api.search('$aapl')
    elif symbol == 'GOOG':
        public_tweets = api.search('$goog')
    elif symbol == 'SPY':
        public_tweets = api.search('$spy')
    elif symbol == 'DIS':
        public_tweets = api.search('$dis')
    elif symbol == 'FB':
        public_tweets = api.search('$fb')
    elif symbol == 'AMZN':
        public_tweets = api.search('$amzn')
    elif symbol == 'MSFT':
        public_tweets = api.search('$msft')

    # Find tweets and catorgorize them
    neg_count = 0
    pos_count = 0
    tweets_pos = []
    tweets_neg = []
    for tweet in public_tweets:
        #Step 4 Perform Sentiment Analysis on Tweets
        analysis = TextBlob(tweet.text)
        if (analysis.polarity > 0 and analysis.subjectivity > 0.25):
            pos_count += 1
            tweets_pos.append(tweet.text)
        elif (analysis.polarity < 0 and analysis.subjectivity > 0.25):
            neg_count += 1
            tweets_neg.append(tweet.text)


    twitter_sentiment_pos_neg = { '# of Positive Tweets': pos_count, '# of Negative Tweets': neg_count, 'Positive Tweets': tweets_pos, 'Negative Tweets': tweets_neg }
    return twitter_sentiment_pos_neg
