
# ElectricMotorTempPrediction

A Flask-based machine learning web application that predicts the internal temperature of an electric motor using Random Forest Regression. The model is trained on real-time sensor data including voltage, current, torque, speed, and various temperature readings.

---

## 🚀 Project Objective

To develop a predictive system for electric motor temperature monitoring to prevent failures and optimize motor performance using machine learning.

---

## 🔍 Features

- Predicts motor and component temperatures from sensor inputs  
- Web-based UI for input and result display  
- Built with Flask, Python, and Scikit-learn  
- Trained using Random Forest Regression model

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Regressor  
- **Training Dataset**: Includes features like voltage, current, torque, speed, stator_yoke, stator_winding, and stator_tooth temperatures.  
- **Target Variable**: Motor temperature

---

## 📂 Project Structure

```
ElectricMotorTempPrediction/
├── app.py                      # Flask web app
├── data.csv                   # Dataset file
├── model/
│   └── model.save             # Trained ML model
├── templates/
│   ├── index.html             # User input form
│   └── result.html            # Result display
├── notebook/
│   └── Rotor_motor_temp_detection.ipynb  # Training notebook
├── requirement.txt            # Python dependencies
└── README.md                  # Project overview
```

---

## ⚙️ How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/ketan1819/ElectricMotorTempPrediction.git
   ```

2. Navigate to the project directory  
   ```bash
   cd ElectricMotorTempPrediction
   ```

3. Install dependencies  
   ```bash
   pip install -r requirement.txt
   ```

4. Run the Flask app  
   ```bash
   python app.py
   ```

5. Open in browser  
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Screenshots

> Screenshots of UI (upload these into a `/screenshots/` folder or directly embed them below):

- **Home Page (User Input)**
- **Prediction Output Page**

---

## 🎬 Demo Video (Optional)

If you have recorded a demo video, upload it to YouTube or Google Drive and paste the link here.

---

## 🔗 Hosted Link (Optional)

If you deployed your app (e.g., on Render, Replit, or Railway), paste the link here:

```
https://your-deployed-app-link.com
```

---

## ✒️ Author

- **Ketan** – [GitHub Profile](https://github.com/ketan1819)

---

## 📌 License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
