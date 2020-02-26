"""Home routes"""

import os

from flask import Blueprint, render_template, send_from_directory

from twitoff.models import Tweeter

home_routes = Blueprint('home_routes', __name__)


@home_routes.route('/')
def home():
    """Returns rendered home.html template."""
    tweeters = []
    for tweeter in Tweeter.query.all():
        tweeters.append(tweeter.screen_name)
    return render_template(
        'home.html',
        tweeters=tweeters
    )


@home_routes.route('/favicon.ico')
def favicion():
    """Returns favicon.ico from static directory."""
    return send_from_directory(
        os.path.join(os.path.join(app.root_path, 'static')),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
