# -*- coding: utf-8 -*-
"""Sample flask app."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    """Welcome page handler."""
    return "Container works!!!"


if __name__ == "__main__":
    app.run()
