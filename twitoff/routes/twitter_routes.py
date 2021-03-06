"""Twitter routes (FLASK)."""

from flask import Blueprint, render_template, request, url_for

from twitoff.basilica_service import basilica_api
from twitoff.models import Tweet, Tweeter, db
from twitoff.twitter_service import get_timeline, get_user, twitter_api

twitter_routes = Blueprint('twitter_routes', __name__)


def model_to_dict(model):
    d = model.__dict__
    if '_sa_instance_state' in d.keys():
        del d['_sa_instance_state']
    return d


@twitter_routes.route('/tweeters/')
def get_all_tweeters():
    tweeters = []
    all_tweeters = Tweeter.query.all()
    for tweeter in all_tweeters:
        t = model_to_dict(tweeter)
        tweeters.append(t)
    return render_template(
        'tweeters.html',
        tweeters=tweeters
    )


@twitter_routes.route('/tweeters/<screen_name>')
def get_tweeter(screen_name=None):
    tweets = []
    messages = []
    tweeter = {
        'screen_name': screen_name,
        'name': '',
        'followers_count': 0,
        'statuses_count': 0,
        'stored_count': 0,
        'id': 0,
        'id_str': 0,
        'latest_status_id': 0
    }
    db_tweeter = Tweeter.query.filter_by(screen_name=screen_name).first()
    # not in database, query twitter
    if db_tweeter is None:
        user = get_user(screen_name=screen_name)
        # user not found through twitter api
        if user is None:
            messages.append(f'Unable to find Twitter account: {screen_name}')
        # found user, check if protected
        elif user.protected:
            messages.append(f'Unable to load tweets for {screen_name}.')
            messages.append('Account is protected.')
        # found user, add to database
        else:
            tweeter['screen_name'] = user.screen_name
            tweeter['name'] = user.name
            tweeter['followers_count'] = user.followers_count
            tweeter['statuses_count'] = user.statuses_count
            tweeter['id'] = user.id
            new_tweeter = Tweeter(
                screen_name=user.screen_name,
                name=user.name,
                id=user.id,
                id_str=user.id_str,
                followers_count=user.followers_count,
                statuses_count=user.statuses_count
            )
            db.session.add(new_tweeter)
            db.session.commit()
    # found screen_name in database
    else:
        tweeter['screen_name'] = db_tweeter.screen_name
        tweeter['name'] = db_tweeter.name
        tweeter['followers_count'] = db_tweeter.followers_count
        tweeter['statuses_count'] = db_tweeter.statuses_count
        tweeter['id'] = db_tweeter.id

    # valid tweeter
    if tweeter['id'] != 0:
        timeline = get_timeline(tweeter['screen_name'])
        tweets = [status.full_text for status in timeline]
        if len(tweets) > 0:
            b_api = basilica_api()
            embeddings = list(b_api.embed_sentences(tweets, model='twitter'))
            for status, embedding in zip(timeline, embeddings):
                new_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
                new_tweet.id_str = status.id_str
                new_tweet.text = status.full_text
                new_tweet.tweeter_id = status.author.id
                new_tweet.embedding = embedding
                db.session.add(new_tweet)
                db.session.commit()
        elif len(tweets) != len(timeline):
            messages.append('mismatch size of timeline and tweets')
            messages.append(f'timeline: {len(timeline)}')
            messages.append(f'tweets: {len(tweets)}')
        else:
            messages.append(f'No tweets loaded for {screen_name}')

    return render_template(
        'tweeter.html',
        tweeter=tweeter,
        tweets=tweets,
        messages=messages
    )
