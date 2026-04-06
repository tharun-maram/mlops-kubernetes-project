from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Dummy model logic (same as training)
def predict(x):
    return 2 * x  # since model learned y = 2x

@app.route("/")
def home():
    return "ML API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    value = data.get("value")

    result = predict(value)

    return jsonify({
        "input": value,
        "prediction": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
