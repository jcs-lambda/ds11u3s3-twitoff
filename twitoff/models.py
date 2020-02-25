"""Database"""

import re

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

HANDLE_PATTERN = re.compile('^[a-zA-Z0-9_]{1,15}$')

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
    # fields
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(15), unique=True, nullable=False)
    name = db.Column(db.String(50))
    # back references
    tweets = db.relationship('Tweet', backref='tweeter', lazy=True)
    # validation properties
    _messages = []
    _handle_pattern = re.compile('^[a-zA-Z0-9_]{1,15}$')
    _name_pattern = re.compile('^.{,50}$')

    def _is_valid_handle(self):
        """Returns True if handle is valid, False otherwise."""
        valid = False
        try:
            if self.handle is None:
                raise TypeError('handle is none')
            if not isinstance(self.handle, str):
                raise TypeError('handle is not str')
            if not self._handle_pattern.match(self.handle):
                raise ValueError(f'handle "{self.handle}" not match pattern')
            valid = True
        except Exception as ex:
            self._messages.append('error validating handle')
            self._messages.append(ex)
            self._messages.append(f'handle: {self.handle}')
            self._messages.append(f'type: {type(self.handle)}')
            self._messages.append(f'len: {len(self.handle)}')
        finally:
            return valid

    def _is_valid_name(self):
        """Returns True if name is valid, False otherwise."""
        valid = False
        if self.name is None:
            return True
        try:
            if not isinstance(self.name, str):
                raise TypeError('name is not str')
            if not self._name_pattern.match(self.name):
                raise ValueError(f'name "{self.name}" not match pattern')
            valid = True
        except Exception as ex:
            self._messages.append('error validating name')
            self._messages.append(ex)
            self._messages.append(f'name: {self.name}')
            self._messages.append(f'type: {type(self.name)}')
            self._messages.append(f'len: {len(self.name)}')
        finally:
            return valid

    @property
    def valid(self):
        """Returns True if all self validation passes, False otherwise."""
        return self._is_valid_handle() and self._is_valid_name()

    @property
    def messages(self):
        """Clears and returns an instance's message queue."""
        m = self._messages
        self._messages = []
        return m


class Tweet(db.Model):
    """Tweet table"""
    __tablename__ = 'tweet'
    # fields
    id = db.Column(db.Integer, primary_key=True)
    tweeter_id = db.Column(db.Integer(), db.ForeignKey('tweeter.id'),
                           nullable=False)
    content = db.Column(db.String(280), nullable=False)
    # validation properties
    _messages = []
    _content_pattern = re.compile('^.{1,280}$')

    def _is_valid_tweeter_id(self):
        """Returns True if tweeter_id is valid, False otherwise."""
        valid = False
        try:
            if self.tweeter_id is None:
                raise TypeError('tweeter_id is none')
            if not isinstance(self.tweeter_id, int):
                raise TypeError('tweeter_id is not int')
            # TO DO: check if tweeter_id in Tweeter table
            valid = True
        except Exception as ex:
            self._messages.append('error validating tweeter_id')
            self._messages.append(ex)
            self._messages.append(f'tweeter_id: {self.tweeter_id}')
            self._messages.append(f'type: {type(self.tweeter_id)}')
        finally:
            return valid

    def _is_valid_content(self):
        """Returns True if content is valid, False otherwise."""
        valid = False
        try:
            if self.content is None:
                raise TypeError('content is none')
            if not isinstance(self.content, str):
                raise TypeError('content is not str')
            if not self._content_pattern.match(self.content):
                raise ValueError(f'content "{self.content}" no match pattern"')
            valid = True
        except Exception as ex:
            self._messages.append('error validating content')
            self._messages.append(ex)
            self._messages.append(f'content: {self.content}')
            self._messages.append(f'type: {type(self.content)}')
            self._messages.append(f'len: {len(self.content)}')
        finally:
            return valid

    @property
    def valid(self):
        """Returns true if all self validation passes, False otherwise."""
        return self._is_valid_tweeter_id() and self._is_valid_content()

    @property
    def messages(self):
        """Clears and returns an instance's message queue."""
        m = self._messages
        self._messages = []
        return m
