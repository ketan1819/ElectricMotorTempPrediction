from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import requests

app = Flask(__name__)

# Model download configuration
MODEL_URL = "https://drive.google.com/uc?export=download&id=16naK6NUPZCwyMirlZSiDt0_ORTomw3XK"
MODEL_PATH = os.path.join('model', 'model.save')

# Ensure the model directory exists
os.makedirs('model', exist_ok=True)

# Download model if not already present
if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    response = requests.get(MODEL_URL)
    if response.status_code == 200:
        with open(MODEL_PATH, 'wb') as f:
            f.write(response.content)
        print("Model downloaded successfully.")
    else:
        raise Exception("Failed to download the model from Google Drive.")

# Load the model
model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all 11 input features from form
        input_features = [
            float(request.form['u_q']),
            float(request.form['coolant']),
            float(request.form['stator_winding']),
            float(request.form['u_d']),
            float(request.form['stator_tooth']),
            float(request.form['motor_speed']),
            float(request.form['i_d']),
            float(request.form['i_q']),
            float(request.form['stator_yoke']),
            float(request.form['ambient']),
            float(request.form['torque'])
        ]

        # Reshape input for model
        final_input = np.array(input_features).reshape(1, -1)

        # Predict
        prediction = model.predict(final_input)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
