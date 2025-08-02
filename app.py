from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import gdown  # ✅ added gdown

app = Flask(__name__)

# ✅ Google Drive file ID (from your model link)
FILE_ID = "16naK6NUPZCwyMirlZSiDt0_ORTomw3XK"
MODEL_PATH = os.path.join('model', 'model.save')

# ✅ Ensure model directory exists
os.makedirs('model', exist_ok=True)

# ✅ Download model using gdown
if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", MODEL_PATH, quiet=False)
    print("Model downloaded successfully.")

# ✅ Load model
model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
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
        final_input = np.array(input_features).reshape(1, -1)
        prediction = model.predict(final_input)[0]
        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
