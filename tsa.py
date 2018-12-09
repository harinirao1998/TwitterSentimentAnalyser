import tweepy
from textblob import TextBlob
import csv

consumer_key='RDoAThkkhWdU7m9L45aKu4hZ0'
consumer_secret='wzRhOKaxpwVdSSMF25AwwWVqf5M8QQVLJrZ18fSTngfj94bjzn'

access_token='2215797192-Xmvho9WdMa4v5VQ89LjeHE5iuz51qkjtQxeOJH5'
access_token_secret='CD14EHx0MywhKAk4aKC9qPp6G53Ut691xl1cgJR0pdDBv'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


tweet_search_topic = input("What topic you want to find ? : ")


public_tweets = api.search(tweet_search_topic)


with open('dataset.csv', mode='w') as tweets_file:
    tweet_writer = csv.writer(tweets_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    
    tweet_writer.writerow(['Tweet', 'Author', 'Date', 'Sentiment Polarity'])
    
    for tweet in public_tweets:
        tweet_text = tweet.text
        tweet_user = tweet.user.name
        tweet_created_at = tweet.created_at
        tweet_sentiment = TextBlob(tweet_text).sentiment.polarity
        print(tweet_text, tweet_user, tweet_created_at)
        print("Sentiment is %f" % tweet_sentiment)
        tweet_writer.writerow([tweet_text, tweet_user, tweet_created_at, tweet_sentiment])
    
