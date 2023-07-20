# PIP INSTALL tweepy
# create a twitter API

# NOTE: twitter API is now a paid service hence, do not have access to API keys
import tweepy
import time

consumer_key = '<enter>'
consumer_secret = '<enter>'
access_token = '<enter>'
access_token_secret = '<enter>'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
# print (user.name)
# print (user.screen_name)
# print (user.followers_count)

search = "Yusuf Kathrada"
numberOfTweets = 2

# Used in order to not make too many requests to API
def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Follow back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Retweet posts that have the var "search"
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
