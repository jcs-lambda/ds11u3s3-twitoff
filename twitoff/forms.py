"""Forms for user input.

Uses WTForms.
"""

import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

SCREEN_NAME_VALIDATORS = [
    DataRequired(message='Required'),
    Length(
        min=1,
        message='at least %(min)d characters'
    ),
    Regexp(
        regex=re.compile('^[a-z0-9_]+', re.IGNORECASE),
        message='only alpha-numeric and _'
    )
]


class AddTweeterForm(FlaskForm):
    screen_name = StringField(
        label='Screen Name',
        validators=SCREEN_NAME_VALIDATORS,
        description='Twitter screen name',
        id='screen_name_add',
    )
    submit = SubmitField(
        label='Add Tweeter',
        description='Add Tweeter',
        id='submit_tweeter'
    )


class PredictForm(FlaskForm):
    tweeter_1 = StringField(
        label='Screen Name 1',
        validators=SCREEN_NAME_VALIDATORS,
        description='Twitter screen name',
        id='screen_name_1',
    )
    tweeter_2 = StringField(
        label='Screen Name 2',
        validators=SCREEN_NAME_VALIDATORS,
        description='Twitter screen name',
        id='screen_name_2',
    )
    fake_tweet = StringField(
        label='Tweet',
        validators=[
            DataRequired(message='Required'),
            Length(
                min=1,
                max=240,
                message='between %(min)d and %(max)d characters'
            ),
        ],
        description='Tweet to predict authorship for.',
        id='fake_tweet'
    )
    submit = SubmitField(
        label='Predict',
        description='Predict authorship of tweet',
        id='submit_predict'
    )
