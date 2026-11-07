import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>八幡平　産直掲示板</h1><ul>{omikujis}</ul><p>こんばんは</p>"


@app.route("/omikuji")
def hello():
    omikujis = ["大吉", "中吉", "吉", "凶"]
    unnsei = random.choice(omikujis)
    return f"<p>あなたの運勢は{unnsei}</p>"
