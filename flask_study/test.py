# -*- coding: utf-8 -*-
"""
__author__ = Zhouxiaoguang
__time__ = 18-3-26 下午6:17
__file__ = test.py
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

if __name__ == '__main__':
    app.run(debug=True)