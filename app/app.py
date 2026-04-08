from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("../index.html")   # simple direct file serve

@app.route("/health")
def health():
    return jsonify(status="OK")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)