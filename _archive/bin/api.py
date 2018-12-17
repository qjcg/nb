#!/usr/bin/env python3
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('Hello <b>{{name}}</b>!', name=name)

run(host='localhost', port=8080)
