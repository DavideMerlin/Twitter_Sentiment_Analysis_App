import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'Insert_Key_Here'
consumer_secret= 'Insert_Secret_Here'

access_token='Insert_Key_Here'
access_token_secret='Insert_Secret_Here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')


for tweet in public_tweets:
    print(tweet.text)


    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
