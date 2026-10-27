from flask import Flask, request, jsonify

app = Flask(__name__)


# GET endpoint
@app.get("/hello")
def hello():
    # Get optional name from URL
    name = request.args.get("name", "world")
    return jsonify({"message": f"Hello, {name}!", "status": "success"})


# POST endpoint
@app.post("/sum")
def sum_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    numbers = data.get("numbers")

    total = sum(numbers)

    return jsonify({"sum": total, "status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
