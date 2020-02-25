# ds11u3s3-twitoff
DS11 Unit 3 Sprint 3 - Twitter Face-Off

### Obtain API keys
[AlphaVantage](https://www.alphavantage.co/support/#api-key)

[Basilica](https://www.basilica.ai/api-keys/)

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

[Browse your local app](http://127.0.0.1:5000/)
