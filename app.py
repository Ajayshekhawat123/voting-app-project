from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import redis

app = Flask(__name__)
socketio = SocketIO(app)
redis_client = redis.StrictRedis(host="your_redis_host", port=6379, db=0)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("vote")
def handle_vote(option):
    redis_client.publish("votes", option)
    emit("vote", option, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
