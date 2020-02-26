"""Flask routes for /iris urls.

Demonstrate serialization of predictive model.
"""

from flask import Blueprint
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris_routes = Blueprint('iris_routes', __name__)


@iris_routes.route('/iris')
def iris():
    """Returns string of a prediction."""
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(
        random_state=0,
        solver='lbfgs',
        multi_class='multinomial'
    ).fit(X, y)
    return str(clf.predict(X[:2, :]))
