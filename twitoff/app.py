"""Flask application core logic."""

import os

from dotenv import load_dotenv
from flask import Flask, url_for

from twitoff.models import db, migrate
from twitoff.routes.home_routes import home_routes
from twitoff.routes.twitter_routes import twitter_routes

assert load_dotenv(), 'falied to initialize environment'
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')


def create_app():
    """Create and configure a Flask application instance.

    Returns:
    Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    # configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    # configure routes
    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)

    return app
