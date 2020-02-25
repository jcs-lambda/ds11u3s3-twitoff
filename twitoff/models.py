"""Database"""

import re

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

HANDLE_PATTERN = re.compile('^[a-zA-Z0-9_]{1,15}$')

class Tweeter(db.Model):
    """Tweeter table"""
    __tablename__ = 'tweeter'
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(15), unique=True, nullable=False)
    name = db.Column(db.String(50))
    tweets = db.relationship('Tweet', backref='tweeter', lazy=True)

    def __init__(self, handle:str, name:str =None, **kwargs):
        """Initialize and instance with a (required) handle and name."""
        super(Tweeter, self).__init__(**kwargs)
        if name is not None:
            assert isinstance(name, str)
            assert len(name) <= 50
        assert isinstance(handle, str)
        assert  bool(HANDLE_PATTERN.match(handle)) == True
        self.handle = handle
        self.name = name


class Tweet(db.Model):
    """Tweet table"""
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    tweeter_id = db.Column(db.Integer(), db.ForeignKey('tweeter.id'), nullable=False)
    content = db.Column(db.String(140))
