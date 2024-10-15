import os
from datetime import timedelta

import redis
from flask import Flask, session
from flask_session import Session


app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_PERMANENT_TIMEOUT'] = timedelta(minutes=1)
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://127.0.0.1:6379')

Session(app)

@app.route("/get")
def get():
    return f"server1 {session.get('user')}"

@app.route('/set')
def set():
    session['user'] = "Mondal"
    return "Done"

if __name__ == "__main__":
    app.run(port=5001)