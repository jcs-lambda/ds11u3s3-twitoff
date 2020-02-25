"""Tweeter routes"""

import os

from flask import Blueprint, render_template, request, send_from_directory

from twitoff.models import Tweet, Tweeter, db

tweeter_routes = Blueprint('tweeter_routes', __name__)


def get_all_with_num_tweets():
    """Returns rows from tweeter table as list of dicts."""
    rows = []
    for row in Tweeter.query.all():
        r = {
            'handle': row.handle,
            'name': row.name,
            'tweeter_url': '/tweeter/' + row.handle,
            'num_tweets': Tweet.query.filter_by(tweeter_id=row.id).count()
        }
        rows.append(r)
    return rows


@tweeter_routes.route('/tweeter/')
@tweeter_routes.route('/tweeter', methods=['GET', 'POST'])
def tweeter():
    """Returns rendered tweeter.html template."""
    messages = []
    if request.method == "POST":
        handle = request.form['handle']
        new_tweeter = Tweeter(
            handle=handle,
            name='TODO: get name from twitter'
        )
        if not new_tweeter.valid:
            messages = messages + new_tweeter.messages
        elif Tweeter.query.filter_by(handle=handle).first() is None:
            db.session.add(new_tweeter)
            db.session.commit()
        else:
            message = f'tweeter "{handle}" already exists.'
            messages.append(message)
    return render_template(
        'tweeter.html',
        tweeters=get_all_with_num_tweets(),
        messages=messages
    )


@tweeter_routes.route('/tweeter/<handle>')
def a_tweeter():
    """Renders a specific users tweets."""
    pass
