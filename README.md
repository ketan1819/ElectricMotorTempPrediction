
# 🔧 Electric Motor Temperature Prediction Web App

A **Machine Learning-powered Flask web application** that predicts the temperature of electric motors using key performance parameters such as voltage, current, torque, and speed. Built as part of an experiential learning internship project.

---

## 🚀 Project Objective

To design and deploy a predictive model for electric motor temperature using **Random Forest Regression Model** and serve predictions through a user-friendly **Flask web application**.

🌐 Live Demo: [Video Demo on Google Drive](https://drive.google.com/drive/folders/1gk4LbHX-LQFN8aQPQXoP7ouJ1zy9Nslp?usp=sharing)  
📸 Screenshots: [Screenshots Folder](https://drive.google.com/drive/folders/1kXAT0e9yQobW273-G6vaZXgs1FnqEkQD?usp=sharing)  
📦 Dataset: [Kaggle Dataset](https://www.kaggle.com/wkirgsn/electric-motor-temperature)  
📁 Model File: [model.save on Google Drive](https://drive.google.com/file/d/1Udpfrar06AOC-YxZEyobbErAoYF3SA-v/view?usp=sharing)

---

## 📁 Project Structure

```
ElectricMotorTempPrediction/
│
├── app.py                           # Flask app code
├── model/
│   └── model.save                   # Trained SVR model file
├── templates/
│   ├── index.html                   # User input form
│   └── result.html                  # Prediction result page
├── css/
│   └── style.css                    # Optional styling for frontend
├── notebook/
│   └── Rotor_motor_temp_detection.ipynb  # EDA + Model Training
├── data.csv                         # Dataset (external link provided)
├── requirement.txt                  # Python dependencies
├── README.md                        # Project documentation
```

---

## 🧠 Technologies Used

- **Python 3.12**
- **Flask** – Web Framework
- **Scikit-learn** – Model Training (SVR)
- **Pandas, NumPy** – Data Manipulation
- **Matplotlib** – Visualization
- **HTML/CSS** – Frontend Templating (Jinja2)
- **Jupyter Notebook** – Experimentation & Training

---

## 📊 Dataset Used

We used a public dataset from Kaggle for electric motor temperatures:  
🔗 [Electric Motor Temperature Dataset](https://www.kaggle.com/wkirgsn/electric-motor-temperature)

Since GitHub doesn’t allow files over 25MB, the dataset was not uploaded here.

---

## ⚙️ How It Works

1. **Model Training**: Random Forest Model in `Rotor_motor_temp_detection.ipynb` and saved.
2. **Prediction Logic**: User inputs values via `index.html`.
3. **Model Prediction**: `model.save` is loaded in `app.py`, generates output.
4. **Result Displayed**: Output shown on `result.html` page.

---

## 🖥️ Running the Project Locally

### 🔧 Prerequisites

Ensure Python 3.12+ is installed. Then run:

```bash
# Clone the repository
git clone https://github.com/your-username/ElectricMotorTempPrediction

cd ElectricMotorTempPrediction

# Install all required dependencies
pip install -r requirement.txt

# Run the Flask app
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

---

## 📸 Screenshots

🔗 [Click to View Screenshots Folder](https://drive.google.com/drive/folders/1kXAT0e9yQobW273-G6vaZXgs1FnqEkQD?usp=sharing)

---

## 🎥 Project Demo Video

🔗 [Click to Watch the Demo on Google Drive](https://drive.google.com/drive/folders/1gk4LbHX-LQFN8aQPQXoP7ouJ1zy9Nslp?usp=sharing)

---
If you'd like to retrain:

Open notebook/Rotor_motor_temp_detection.ipynb

Train model on full dataset

Export model to model/model.save
---

## 📌 Key Learnings

- Hands-on experience with **Random Forest Regression Model**
- **End-to-End Machine Learning Lifecycle**: Data cleaning, feature selection, training, deployment
- Serving predictions with **Flask and HTML templates**
- Working with **GitHub**, **Google Drive**, and **Kaggle** integration

---

## 🙌 Acknowledgments

This project was developed under the guidance of mentors as part of the **Experiential Learning Internship Program**.

---

## 👤 Author

- **Name**: *[Ketan Sonawane And Team]*  
- **GitHub**: [ketan1819](https://github.com/ketan1819)
