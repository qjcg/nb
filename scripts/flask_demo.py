#!/usr/bin/env python3
"""Demo of basic Flask functionality.
"""

import subprocess
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    return "{'status': 'awesome'}"


@app.route("/users/<name>", methods=["GET"])
def greet(name="James"):
    return "Hello, {}\n".format(name)


@app.route("/user/", methods=["POST"])
def user():
    return str(request.form)


@app.route("/uptime", methods=["GET"])
def uptime():
    return subprocess.run('uptime', capture_output=True).stdout.decode()


@app.route("/squared/<int:num>", methods=["POST"])
def squared(num):
    return str(num ** 2) + '\n'


if __name__ == "__main__":
    app.run()
