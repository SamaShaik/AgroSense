from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load saved model and scaler
model_path = os.path.join("model", "model.pkl")
scaler_path = os.path.join("model", "minmaxscaler.pkl")

model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))

# Crop dictionary
crop_dict = {
    1: 'rice', 2: 'maize', 3: 'chickpea', 4: 'kidneybeans', 5: 'pigeonpeas',
    6: 'mothbeans', 7: 'mungbean', 8: 'blackgram', 9: 'lentil', 10: 'pomegranate',
    11: 'banana', 12: 'mango', 13: 'grapes', 14: 'watermelon', 15: 'muskmelon',
    16: 'apple', 17: 'orange', 18: 'papaya', 19: 'coconut', 20: 'cotton',
    21: 'jute', 22: 'coffee'
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosphorus'])
    K = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    pH_Value = float(request.form['pH_Value'])
    Rainfall = float(request.form['Rainfall'])

    # Prepare and scale features
    features = np.array([[N, P, K, Temperature, Humidity, pH_Value, Rainfall]])
    scaled_features = scaler.transform(features)

    # Predict crop
    pred = model.predict(scaled_features)[0]
    crop_name = crop_dict[pred]

    return render_template('index.html', prediction_text=f"Recommended Crop: {crop_name}")

if __name__ == "__main__":
    app.run(debug=True)
