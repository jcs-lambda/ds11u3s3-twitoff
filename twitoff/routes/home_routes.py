"""Home routes"""

import os
import sys

from flask import (Blueprint, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)

from twitoff.forms import AddTweeterForm, PredictForm
from twitoff.models import Tweeter

home_routes = Blueprint('home_routes', __name__)


@home_routes.route('/', methods=['GET'])
def home_get():
    """Handle home page GET request."""
    tweeters = []
    for tweeter in Tweeter.query.all():
        tweeters.append(tweeter.screen_name)
    return render_template(
        'home.html',
        tweeters=tweeters,
        form_add_tweeter=AddTweeterForm(),
        form_predict=PredictForm(),
    )


@home_routes.route('/', methods=['POST'])
def home_post():
    """Handle home page POST request."""
    # add user
    if 'screen_name' in request.form.keys():
        return redirect(url_for('twitter_routes.get_tweeter', screen_name=request.form['screen_name']))
    else:
        return redirect(url_for('home_routes.home_get'))


@home_routes.route('/favicon.ico')
def favicion():
    """Returns favicon.ico from static directory."""
    return redirect(url_for('static', filename='favicon.ico'))
    # return send_from_directory(
    #     os.path.join(os.path.join(app.root_path, 'static')),
    #     'favicon.ico',
    #     mimetype='image/vnd.microsoft.icon'
    # )
