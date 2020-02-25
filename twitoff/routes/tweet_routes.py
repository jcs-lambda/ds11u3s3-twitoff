"""Tweeter routes"""

import os

from flask import Blueprint, render_template, send_from_directory

from twitoff.models import Tweet, db, get_all

tweet_routes = Blueprint('tweet_routes', __name__)


def get_all_with_name():
    """Return joined rows from tweet and user table."""
    rows = []
    for row in Tweet.query.all():
        r = {
            'handle': row.tweeter.handle,
            'tweeter_url': '/tweeter/' + row.tweeter.handle,
            'content': row.content,
            'name': row.tweeter.name,
        }
        rows.append(r)
    return rows


@tweet_routes.route('/tweets/')
@tweet_routes.route('/tweet/')
def tweet():
    """Returns rendered tweet.html template."""
    return render_template('tweet.html', tweets=get_all_with_name())
