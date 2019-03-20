from flask import Flask


"""
export FLASK_APP=web
export FLASK_ENV=development
flask run
"""


def create_app():
    app = Flask(__name__)

    from . import books
    app.register_blueprint(books.bp)

    return app
