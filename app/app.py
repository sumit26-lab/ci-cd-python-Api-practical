from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    if request.headers.get("Accept") == "application/json":
        return jsonify(message="Hello DevOps Engg")

    return render_template("index.html")   # ✅ FIXED

@app.route("/health")
def health():
    return jsonify(status="OK")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
