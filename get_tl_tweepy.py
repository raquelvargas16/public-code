from tweepy import API
from tweepy import OAuthHandler
import twitter_credentials #file with your credentials
import json

"""
The TwitterClient and TwitterAuthenticator classes are used to access Twitter data
"""
class TwitterClient():
    def  __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

class TweetAnalyzer():
    """
    By iterating on the Tweepy ResultSet, we define the following function to preprocess the tweets and just get:
     the text, the date of creation, the id and the language of each tweet.
    """
    def tweets_to_dict(self,tweets):
        items = ["text", "created_at", "id", "lang"]
        tl_tweets = [] # store the tweets in a list
        for tweet in tweets:
            tweet_f = dict((key,value) for key, value in tweet._json.items() if key in items) #"filter" the dictionary by "items"
            tweet_f.update({"contenttype": "text/plain"})
            tl_tweets.append(tweet_f)
        return tl_tweets

if __name__ == '__main__':
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name="ladygaga", count=200)
    ladygaga_tl = tweet_analyzer.tweets_to_dict(tweets)
    print(ladygaga_tl)
    with open('tweets_ladygaga.json', 'w') as outfile:  # Save the results to a json file
       json.dump(ladygaga_tl, outfile)
