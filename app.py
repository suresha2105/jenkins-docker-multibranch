from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker Multibranch Pipeline!"

@app.route("/health")
def health():
    return "Healthy", 200

@app.route("/branch")
def branch():
    return os.getenv("APP_BRANCH", "unknown"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

