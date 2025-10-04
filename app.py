from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello from GitHub Actions!</h1><p>This page was updated at: {now}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)