# coding: UTF-8

from flask import Flask

"""
hello.py
Flask+SQLite3でWeb-DBアプリ開発
日経ソフトウェア2019年3月号
Copyright (C) 2019 J.Kawahara
2019.3.19 J.Kawahara 新規作成
"""

"""
    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run
"""

myapp = Flask(__name__)
# myapp.config.from_object('config.DevelopmentConfig')


@myapp.route('/')
def index():
    return 'こんにちは'
