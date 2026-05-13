from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Calculator API",
        "endpoints": ["/add", "/subtract", "/multiply", "/divide"]
    })


@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"operation": "addition", "a": a, "b": b, "result": a + b})


@app.route("/subtract")
def subtract():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"operation": "subtraction", "a": a, "b": b, "result": a - b})


@app.route("/multiply")
def multiply():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"operation": "multiplication", "a": a, "b": b, "result": a * b})


@app.route("/divide")
def divide():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    return jsonify({"operation": "division", "a": a, "b": b, "result": a / b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
