# ds11u3s3-twitoff
DS11 Unit 3 Sprint 3 - Twitter Face-Off

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
