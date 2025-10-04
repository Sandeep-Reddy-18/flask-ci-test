from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Change the message one more time
    return f"<h1>SUCCESS! Fully automated deployment works! Timestamp: {now}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)