"""Database"""

import re
from datetime import datetime

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from twitoff.twitter_service import get_timeline, get_user

db = SQLAlchemy()
migrate = Migrate()


class Tweeter(db.Model):
    """Tweeter table"""
    __tablename__ = 'tweeter'
    # fields
    id = db.Column(db.BigInteger, primary_key=True)
    id_str = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)
    screen_name = db.Column(db.String, unique=True, nullable=False)
    followers_count = db.Column(db.Integer)
    statuses_count = db.Column(db.Integer)
    latest_status_id = db.Column(db.BigInteger)
    # back references
    tweets = db.relationship('Tweet', backref='tweeter', lazy=True)


class Tweet(db.Model):
    """Tweet table"""
    __tablename__ = 'tweet'
    # fields
    id = db.Column(db.BigInteger, primary_key=True)
    id_str = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.String, nullable=False)
    tweeter_id = db.Column(db.BigInteger, db.ForeignKey('tweeter.id'),
                           nullable=False)
    retrieved = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    embedding = db.Column(db.PickleType)
