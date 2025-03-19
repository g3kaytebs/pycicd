from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/api/data", methods=["GET"])
def get_data():
    sample_data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is a sample data response from the Flask API. your CICD pipeline is working fine.",
    }
    return jsonify(sample_data)


@app.route("/api/data", methods=["POST"])
def create_data():
    new_data = request.json
    response = {"message": "Data created successfully!", "data": new_data}
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
