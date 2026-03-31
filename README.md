# Rainfall Prediction System

A machine learning–powered web application that predicts whether it will rain the **next day** in Australia based on current weather conditions.

---

## Overview

**Rain Predictor** is a Flask web app backed by several trained ML models. It takes meteorological inputs for an Australian location and outputs either a **Sunny Day** or a **Rainy Day** prediction for tomorrow. The project is based on the well-known *Rain in Australia* dataset (`weatherAUS.csv`).

---

## Demo Screenshots

| Dashboard | Predictor Form | Result |
|-----------|---------------|--------|
| ![Dashboard](static/dashboard.png) | *(predictor.html)* | ![Rainy](static/rainy.jpg) |

---

## Features

- **Next-day rain prediction** using a CatBoost classifier (primary model)
- **Interactive web UI** with a clean, responsive design (Bootstrap 5 + Poppins font)
- **Dashboard section** with rainfall visualizations (Power BI report & charts)
- Supports **49 Australian weather stations**
- Encodes categorical inputs (wind direction, location) using label-encoded dropdowns
- Separate result pages for sunny and rainy predictions

---

## Project Structure

```
rainfall-prediction-system/
├── app.py                    # Flask application entry point
├── requirements.txt          # Python dependencies
├── weatherAUS.csv            # Raw dataset (Rain in Australia)
├── RainPrediction2.ipynb     # Main Jupyter notebook (EDA + model training)
├── models/
│   ├── cat.pkl               # CatBoost model (active — used by app)
│   ├── gnb.pkl               # Gaussian Naive Bayes model
│   ├── logreg.pkl            # Logistic Regression model
│   ├── svc.pkl               # Support Vector Classifier model
│   └── xgb.pkl               # XGBoost model
├── template/
│   ├── index.html            # Landing page (Home / About / Dashboard / Developer)
│   ├── predictor.html        # Prediction input form
│   ├── after_rainy.html      # Result page — rain predicted
│   └── after_sunny.html      # Result page — no rain predicted
├── static/
│   ├── style.css / style1.css / predictor.css / after_rainy.css
│   ├── dashboard.png         # Dashboard overview image
│   ├── 1.png – 9.png         # Dashboard chart images
│   ├── rainy.jpg             # Rainy result illustration
│   ├── sunny.jpg             # Sunny result illustration
│   └── rain.pbix             # Power BI dashboard file
└── testing/
    ├── Prediction.ipynb
    ├── Prepocessing.ipynb
    ├── RainPrediction.ipynb
    ├── RainPrediction3.ipynb
    └── weatherAUS.csv
```

---

## Input Features

The predictor form accepts the following 23 features:

| Feature | Description |
|---------|-------------|
| Date | Observation date (day & month extracted) |
| Location | Australian city / weather station |
| MinTemp | Minimum temperature (°C) |
| MaxTemp | Maximum temperature (°C) |
| Rainfall | Amount of rainfall recorded (mm) |
| Evaporation | Evaporation (mm) |
| Sunshine | Sunshine hours |
| WindGustDir | Direction of the strongest wind gust |
| WindGustSpeed | Speed of the strongest wind gust (km/h) |
| WindDir9am / WindDir3pm | Wind direction at 9 AM and 3 PM |
| WindSpeed9am / WindSpeed3pm | Wind speed at 9 AM and 3 PM (km/h) |
| Humidity9am / Humidity3pm | Relative humidity at 9 AM and 3 PM (%) |
| Pressure9am / Pressure3pm | Atmospheric pressure at 9 AM and 3 PM (hPa) |
| Cloud9am / Cloud3pm | Fraction of sky covered by clouds at 9 AM and 3 PM |
| Temp9am / Temp3pm | Temperature at 9 AM and 3 PM (°C) |
| RainToday | Did it rain today? (Yes / No) |

---

## Machine Learning Models

Multiple models were trained and compared during experimentation:

| Model | File |
|-------|------|
| **CatBoost** *(deployed)* | `models/cat.pkl` |
| XGBoost | `models/xgb.pkl` |
| Support Vector Classifier | `models/svc.pkl` |
| Logistic Regression | `models/logreg.pkl` |
| Gaussian Naive Bayes | `models/gnb.pkl` |

The CatBoost model was selected for deployment due to its strong performance on the imbalanced dataset.

---

## Dataset

- **Source:** Rain in Australia — [Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
- **Size:** ~145,000 observations across 49 Australian weather stations
- **Target variable:** `RainTomorrow` (Yes / No)
- **Class imbalance** handled with `imbalanced-learn` (SMOTE / resampling)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, Flask-CORS |
| ML | CatBoost, XGBoost, scikit-learn, imbalanced-learn |
| Data | Pandas, NumPy, Matplotlib, Seaborn, Plotly |
| Frontend | HTML5, CSS3, Bootstrap 5, Jinja2 |
| Deployment | Gunicorn |
| Notebooks | Jupyter |

---

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yatibee/Rainfall-Prediction-System.git
cd Rainfall-Prediction-System
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:<port>` (the port is auto-assigned; check terminal output).

---

## How It Works

1. User visits the **Home** page and navigates to the **Predictor**.
2. User fills in weather details for their Australian location.
3. The form POSTs to `/predict`, where Flask extracts and orders the 23 features.
4. The pre-trained **CatBoost** model (`models/cat.pkl`) makes the prediction.
5. The user is redirected to either `after_rainy.html` or `after_sunny.html`.

---

## Developer

**Yati Singh** — Data Scientist from India, passionate about Machine Learning, Deep Learning, and NLP.

- LinkedIn: [yati-singh-772434291](http://linkedin.com/in/yati-singh-772434291/)
- GitHub: [yatibee](https://github.com/yatibee)

---

## License

This project is open-source. Feel free to use, modify, and distribute it.
