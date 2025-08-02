from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load model
model_path = os.path.join('model', 'model.save')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all 11 feature values from the form
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
        
        # Reshape input to match model's expected format
        final_input = np.array(input_features).reshape(1, -1)

        # Predict
        prediction = model.predict(final_input)[0]

        return render_template('result.html', prediction=round(prediction, 2))
    
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
