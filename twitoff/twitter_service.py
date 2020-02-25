"""Twitter service."""

import os

import tweepy

from dotenv import load_dotenv

# establish environment
assert load_dotenv(), 'failed to initialize environment'
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
assert TWITTER_API_KEY is not None, \
    'falied to load TWITTER_API_KEY from environment'
assert TWITTER_API_SECRET_KEY is not None, \
    'falied to load TWITTER_API_SECRET_KEY from environment'
assert TWITTER_ACCESS_TOKEN is not None, \
    'falied to load TWITTER_ACCESS_TOKEN from environment'
assert TWITTER_ACCESS_TOKEN_SECRET is not None, \
    'falied to load TWITTER_ACCESS_TOKEN_SECRET from environment'


auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

print('PUBLIC TWEETS')
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(type(tweet))
    print(tweet.text)
print('-'*30)

print('USER INFO')
user = api.get_user('Chrisalbon')
print(type(user))
print(user)
print(dir(user))

