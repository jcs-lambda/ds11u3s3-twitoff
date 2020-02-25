"""Twitter service."""

import os

import tweepy
from dotenv import load_dotenv

# establish environment
assert load_dotenv(), 'failed to initialize environment'
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_KEY_SECRET = os.getenv('TWITTER_API_KEY_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
assert TWITTER_API_KEY is not None, \
    'falied to load TWITTER_API_KEY from environment'
assert TWITTER_API_KEY_SECRET is not None, \
    'falied to load TWITTER_API_KEY_SECRET from environment'
assert TWITTER_ACCESS_TOKEN is not None, \
    'falied to load TWITTER_ACCESS_TOKEN from environment'
assert TWITTER_ACCESS_TOKEN_SECRET is not None, \
    'falied to load TWITTER_ACCESS_TOKEN_SECRET from environment'


def twitter_api():
    """Returns an authenticated tweepy.API instance."""
    try:
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN,
                              TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
    except tweepy.error.TweepError as ex:
        print(ex)
        print(ex.response.text)
        api = None
    except Exception as ex:
        print(ex)
        api = None
    finally:
        return api


if __name__ == '__main__':
    api = twitter_api()
    print('PUBLIC TWEETS')
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(type(tweet))
        print(tweet.text)
    print('-'*30)

    print('USER INFO')
    user = api.get_user('Chrisalbon')
    print(type(user))
    print('Screen name:', user.screen_name)
    print('Name:', user.name)
    print('Location:', user.location)
    print('Follower count:', user.followers_count)
