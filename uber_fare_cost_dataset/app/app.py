from flask import Flask, render_template, request, jsonify
from model_loader import load_model
from extra.feature_engineering import haversine


app = Flask(__name__)
model = load_model()


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """Handle fare prediction."""
    try:
        data = request.get_json()  # Get JSON data from the request
        pickup_latitude = float(data["pickup_latitude"])
        pickup_longitude = float(data["pickup_longitude"])
        dropoff_latitude = float(data["dropoff_latitude"])
        dropoff_longitude = float(data["dropoff_longitude"])
        passenger_count = int(data["passenger_count"])

        distance_km = haversine(
            pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude
        )

        features = [[distance_km, passenger_count]]
        predicted_fare = model.predict(features)[0]

        return jsonify({"fare_amount": round(predicted_fare, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
