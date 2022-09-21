# ds11u3s3-twitoff
DS11 Unit 3 Sprint 3 - Twitter Face-Off

# [~~See This App Live, on Heroku~~](https://twitoff-jcslambda.herokuapp.com/) (NO MORE FREE TIER APPS)

## How to use locally
### Obtain API keys
[AlphaVantage](https://www.alphavantage.co/support/#api-key)

[~~Basilica~~](https://www.basilica.ai/api-keys/) (SHUTDOWN)

[Twitter](https://developer.twitter.com/)

### Create file in project root: `.env`
```
FLASK_APP='twitoff'
BASILICA_KEY='<your key here>'
ALPHAVANTAGE_KEY='<your key here>'

TWITTER_API_KEY='<your key here>'
TWITTER_API_KEY_SECRET='<your key secret here>'
TWITTER_ACCESS_TOKEN='<your token here>'
TWITTER_ACCESS_TOKEN_SECRET='<your token secret here>'
```

### Enter the virtual environment
```sh
pipenv shell
```

### Setup / migrate database
```sh
FLASK_APP=twitoff flask db init
FLASK_APP=twitoff flask db migrate
FLASK_APP=twitoff flask db upgrade
```

### Launch app
```sh
FLASK_APP=twitoff flask run
```

### [Browse your local app](http://127.0.0.1:5000/)

## How to deploy to heroku
### From the shell in your project's virtual environment root
```sh
heroku login
heroku create <your-app-name-here>
git push heroku master
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set FLASK_APP='twitoff'
heroku config:set SECRET_KEY='<your key here>'
heroku config:set BASILICA_KEY='<your key here>'
heroku config:set ALPHAVANTAGE_KEY='<your key here>'
heroku config:set TWITTER_API_KEY='<your key here>'
heroku config:set TWITTER_API_KEY_SECRET='<your key here>'
heroku config:set TWITTER_ACCESS_TOKEN='<your key here>'
heroku config:set TWITTER_ACCESS_TOKEN_SECRET='<your key here>'

heroku run /bin/bash
flask db init
flask db stamp head
flask db migrate
flask db upgrade
exit
```

## References
https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object

https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object

http://docs.tweepy.org/en/latest/api.html#api-reference

https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures

https://flask-sqlalchemy.palletsprojects.com/en/2.x/

https://devcenter.heroku.com/articles/heroku-cli
