#!/usr/bin/python

from flask import Flask
import os

app = Flask(__name__)

env = os.getenv("ENV")


@app.route("/")
def home():
    return f"""
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <center>
        <h3>Hello World<br>
            You are connected to <span style="color: green;">{env}</span> environment.</h3>
    </center>
</body>
</html>
"""


@app.route("/healthz")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
