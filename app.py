
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Dummy Model - baad me asli ML model daal denge
def predict_risk(age, location_score, time_night):
    # Simple logic: raat + kam location score = Extreme Risk
    risk_score = (10 - location_score) + (5 if time_night == 1 else 0) + (age/10)
    
    if risk_score > 12:
        return "EXTREME RISK", "red", "Turant 108 pe call karein. Location share ho gayi."
    elif risk_score > 7:
        return "HIGH RISK", "orange", "Alert: Surakshit jagah pe jayein."
    else:
        return "SAFE", "green", "Aap surakshit hain."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    age = int(data.get("age", 20))
    location_score = int(data.get("location_score", 5))
    time_night = int(data.get("time_night", 0))
    
    risk, color, message = predict_risk(age, location_score, time_night)
    
    return jsonify({
        "risk": risk,
        "color": color,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True)
