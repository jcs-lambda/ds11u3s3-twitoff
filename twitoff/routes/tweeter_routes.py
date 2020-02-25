"""Tweeter routes"""

import os

from flask import Blueprint, render_template, request, send_from_directory

from twitoff.models import Tweeter, db, get_all, HANDLE_PATTERN

tweeter_routes = Blueprint('tweeter_routes', __name__)


@tweeter_routes.route('/tweeter/')
@tweeter_routes.route('/tweeter', methods=['GET', 'POST'])
def tweeter():
    """Returns rendered tweeter.html template."""
    if request.method == "POST":
        handle = request.form['handle']
        if (handle is not None and isinstance(handle, str)
            and HANDLE_PATTERN.match(handle)
            and Tweeter.query.filter_by(handle=handle).first() is None):
                new_tweeter = Tweeter(handle)
                db.session.add(new_tweeter)
                db.session.commit()
    return render_template('tweeter.html', tweeters=get_all(Tweeter))
