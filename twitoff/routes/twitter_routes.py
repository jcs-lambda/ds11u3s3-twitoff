"""Twitter routes (FLASK)."""

from flask import Blueprint, render_template,url_for

from twitoff.basilica_service import basilica_api
from twitoff.models import Tweeter, Tweet, db
from twitoff.twitter_service import twitter_api, get_user, get_timeline

twitter_routes = Blueprint('twitter_routes', __name__)


@twitter_routes.route('/tweeters/')
def get_all_tweeters():
    tweeters = []
    all_tweeters = Tweeter.query.all()
    for tweeter in all_tweeters:
        t = tweeter.__dict__
        del t['_sa_instance_state']
        # t['stored_count'] = Tweet.query.filter_by(tweeter_id=t['id']).count()
        tweeters.append(t)
    return render_template(
        'tweeter.html',
        tweeters=tweeters
    )


@twitter_routes.route('/tweeters/<screen_name>')
def get_tweeter(screen_name=None):
    tweets = []
    tweeter = Tweeter.query.filter_by(screen_name=screen_name).first()
    if tweeter is None:
        user = get_user(screen_name=screen_name)
        if user is not None:
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
            tweeter = Tweeter.query.filter_by(screen_name=screen_name).first()
    if tweeter is not None:
        tweeter = tweeter.__dict__
        del tweeter['_sa_instance_state']
        if Tweet.query.filter_by(tweeter_id=tweeter['id']).first() is None:
            timeline = get_timeline(tweeter['screen_name'])
            for tweet in timeline:
                tweets.append(tweet.full_text)
                tweet = Tweet(
                    id=tweet.id,
                    id_str=tweet.id_str,
                    text=tweet.full_text,
                    tweeter_id=tweeter['id'],
                    embedding=list(basilica_api().embed_sentence(tweet.full_text, model='twitter'))
                )
                db.session.add(tweet)
            db.session.commit()
        else:
            for tweet in Tweet.query.filter_by(tweeter_id=tweeter['id']).all():
                tweets.append(tweet.text)         
    return render_template(
        'tweeter.html',
        tweeter=tweeter,
        tweets=tweets
    )
    