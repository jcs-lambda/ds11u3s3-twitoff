"""Database"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def get_all(table):
    """Returns all rows of table_class as a list of dicts.

    Parameters:

    table: SQLAlchemy Model

    Returns:
    list of dicts
    """
    rows = []
    for row in table.query.all():
        r = row.__dict__
        del r['_sa_instance_state']
        rows.append(r)
    return rows


class Tweeter(db.Model):
    """Tweeter table"""
    __tablename__ = 'tweeter'
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(15), unique=True, nullable=False)
    name = db.Column(db.String(50))
    tweets = db.relationship('Tweet', backref='tweeter', lazy=True)


class Tweet(db.Model):
    """Tweet table"""
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    tweeter_id = db.Column(db.Integer(), db.ForeignKey('tweeter.id'), nullable=False)
    content = db.Column(db.String(140))
