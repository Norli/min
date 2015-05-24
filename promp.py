import os
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello bello hello"

if __name__ == "__main__":
    app.run("0.0.0.0", port = 3000, debug = True)