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
    """Returns an authenticated tweepy.API instance.
    
    Returns None on failure.
    """
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


def get_timeline(screen_name: str, since_id=None):
    """Returns list of tweepy.models.Status instances for a given screen name.

    Returns empty list if an error occurs or the name cannot be found.
    """
    if (screen_name is None
        or not isinstance(screen_name, str)
        or screen_name == ''
    ):
        print('twitter_service.get_timeline: invalid screen_name:')
        print(screen_name)
        return None
    try:
        results = twitter_api().user_timeline(
            screen_name=screen_name,
            since_id=since_id,
            tweet_mode='extended',
            count=2000,
            exclude_replies=True,
            include_rts=False
        )
        results = list(results)
    except tweepy.error.TweepError as ex:
        print('twitter_service.get_user:TWEEPY ERROR:')
        print(ex)
        results = []
    except Exception as ex:
        print('twitter_service.get_user:ERROR:')
        print(ex)
        results = []
    finally:
        return results
        

def get_user(screen_name: str):
    """Returns a tweepy.models.User instance for a given screen name.

    Returns None if an error occurs or the name cannot be found.
    """
    if (screen_name is None
        or not isinstance(screen_name, str)
        or screen_name == ''
    ):
        print('twitter_service.get_user: invalid screen_name:')
        print(screen_name)
        return None
    try:
        user = twitter_api().get_user(screen_name=screen_name)
    except tweepy.error.TweepError as ex:
        print('twitter_service.get_user:TWEEPY ERROR:')
        print(ex)
        user = None
    except Exception as ex:
        print('twitter_service.get_user:ERROR:')
        print(ex)
        user = None
    finally:
        return user
        

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
