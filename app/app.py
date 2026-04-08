from flask import Flask, jsonify, send_file, request

app = Flask(__name__)


@app.route("/")
def home():
    # If API client (like pytest) → return JSON
    if request.headers.get("Accept") == "application/json":
        return jsonify(message="Hello DevOps Engg")

    # Otherwise → return HTML
    return send_file("../index.html")


@app.route("/health")
def health():
    return jsonify(status="OK")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)