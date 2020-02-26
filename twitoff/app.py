"""Flask application core logic."""

import os

from flask import Flask

from twitoff.models import db, migrate
from twitoff.routes.home_routes import home_routes
from twitoff.routes.iris_routes import iris_routes
from twitoff.routes.tweet_routes import tweet_routes
from twitoff.routes.tweeter_routes import tweeter_routes
from twitoff.routes.twitter_routes import twitter_routes

DB_FILE = os.path.join(
    os.path.dirname(__file__), '..', 'twitoff.db'
)


def create_app():
    """Create and configure a Flask application instance.

    Returns:
    Flask application instance.
    """
    app = Flask(__name__)

    # configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_FILE
    db.init_app(app)
    migrate.init_app(app, db)

    # configure routes
    app.register_blueprint(home_routes)
    # app.register_blueprint(tweet_routes)
    # app.register_blueprint(tweeter_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(iris_routes)

    return app
