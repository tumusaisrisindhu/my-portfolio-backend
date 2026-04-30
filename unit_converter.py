from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ NEW: converter config (acts like DB)
converter_config = {
    "distance": ["cm", "m", "km"],
    "weight": ["g", "kg"],
    "temperature": ["c", "f"]
}

# Existing conversion logic (only distance for now)
conversion_factors = {
    "cm": 0.01,
    "m": 1,
    "km": 1000
}

# ✅ NEW API → fetch categories + units
@app.route("/converter-config", methods=["GET"])
def get_converter_config():
    return jsonify(converter_config)


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json

    value = float(data["value"])
    from_unit = data["from_unit"]
    to_unit = data["to_unit"]

    base = value * conversion_factors[from_unit]
    result = base / conversion_factors[to_unit]

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)