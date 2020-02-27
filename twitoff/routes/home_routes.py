"""Home routes"""

import os
import sys

from flask import (Blueprint, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)
from sklearn.linear_model import LogisticRegression

from twitoff.basilica_service import basilica_api
from twitoff.forms import AddTweeterForm, PredictForm
from twitoff.models import Tweet, Tweeter, db

home_routes = Blueprint('home_routes', __name__)


@home_routes.route('/', methods=['GET'])
def home_get():
    """Handle home page GET request."""
    tweeters = []
    for tweeter in Tweeter.query.all():
        tweeters.append(tweeter.screen_name)
    return render_template(
        'home.html',
        tweeters=sorted(tweeters),
        form_add_tweeter=AddTweeterForm(),
        form_predict=PredictForm(),
    )


@home_routes.route('/', methods=['POST'])
def home_post():
    """Handle home page POST request."""
    # add user
    if 'screen_name' in request.form.keys():
        return redirect(url_for('twitter_routes.get_tweeter',
                                screen_name=request.form['screen_name']))
    else:
        messages = [
            'screen_name not in POST request',
            str(jsonify(request.form))
        ]
        tweeters = [tweeter.screen_name for tweeter in Tweeter.query.all()]
        return render_template(
            'home.html',
            title='POST ERROR',
            messages=messages,
            tweeters=sorted(tweeters)
        )
        # return redirect(url_for('home_routes.home_get'))


@home_routes.route('/prediction', methods=["POST"])
def prediction_post():
    """Handle prediction page POST request."""
    # invalid POST request = redirect to home page
    if ('tweeter1' not in request.form.keys()
        or 'tweeter2' not in request.form.keys()
        or 'tweet' not in request.form.keys()
        ):
        return redirect(url_for('home_routes.home_get'))
    # get embeddings for user entered tweet
    with basilica_api() as b_api:
        embedding = [list(b_api.embed_sentence(request.form['tweet'],
                                               model='twitter'))]
    # get tweeters from database
    tweeter1 = Tweeter.query.filter(
        Tweeter.screen_name == request.form['tweeter1']).one()
    tweeter2 = Tweeter.query.filter(
        Tweeter.screen_name == request.form['tweeter2']).one()
    # build X features matrix and y target vector
    # features = tweeter's tweets' embeddings
    # target = tweeter
    X_train = []
    y_train = []
    for tweet in tweeter1.tweets:
        X_train.append(tweet.embedding)
        y_train.append(tweeter1.screen_name)
    for tweet in tweeter2.tweets:
        X_train.append(tweet.embedding)
        y_train.append(tweeter2.screen_name)
    # instantiate the model
    # fit the model
    model = LogisticRegression(
        C=0.7,
        random_state=13,
        max_iter=250,
        n_jobs=-1
    ).fit(X_train, y_train)
    # make a prediction
    y_pred = model.predict(embedding)[0]

    tweeters = [tweeter.screen_name for tweeter in Tweeter.query.all()]
    return render_template(
        'home.html',
        tweeters=sorted(tweeters),
        tweet=request.form['tweet'],
        selected_1=request.form['tweeter1'],
        selected_2=request.form['tweeter2'],
        winner=y_pred
    )


@home_routes.route('/favicon.ico')
def favicion():
    """Returns favicon.ico from static directory."""
    return redirect(url_for('static', filename='favicon.ico'))
    # return send_from_directory(
    #     os.path.join(os.path.join(app.root_path, 'static')),
    #     'favicon.ico',
    #     mimetype='image/vnd.microsoft.icon'
    # )


@home_routes.route('/reset')
def reset_get():
    """Resets the database."""
    db.drop_all()
    db.create_all()
    # db.session.commit()
    return render_template(
        'home.html',
        title='Reset',
        messages=['Database Reset Complete.']
    )
