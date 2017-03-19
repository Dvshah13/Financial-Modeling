import tweepy
from textblob import TextBlob

# Authenticate twitter api


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
    for tweet in public_tweets:
        print(tweet.text)
        neg_count = 0
        pos_count = 0
        #Step 4 Perform Sentiment Analysis on Tweets
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        if (analysis.polarity > 0.1 and analysis.subjectivity > 0.4):
            pos_count += 1
        elif (analysis.polarity < 0 and analysis.subjectivity > 0.4):
            neg_count += 1

        print pos_count
        print neg_count
        twitter_sentiment_pos_neg = { 'pos_count': pos_count, 'neg_count': neg_count, 'tweets': tweet.text }
        return twitter_sentiment_pos_neg
