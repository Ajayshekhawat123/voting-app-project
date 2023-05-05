# app.py
from flask import Flask, render_template, request, redirect, url_for
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host="your_redis_host", port=6379, db=0)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vote", methods=["POST"])
def vote():
    option = request.form["option"]
    redis_client.publish("votes", option)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
