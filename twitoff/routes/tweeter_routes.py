"""Tweeter routes"""

import os

from flask import Blueprint, render_template, request, send_from_directory

from twitoff.models import Tweeter, db, get_all

tweeter_routes = Blueprint('tweeter_routes', __name__)


@tweeter_routes.route('/tweeter/')
def tweeter():
    """Returns rendered tweeter.html template."""
    return render_template('tweeter.html', tweeters=get_all(Tweeter))
