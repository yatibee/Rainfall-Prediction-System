from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
import pickle

app = Flask(__name__, template_folder="template")

# Load model
model = pickle.load(open("./models/cat.pkl", "rb"))
print("Model Loaded")

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        # DATE
        date = request.form['date']
        # Handle both "YYYY-MM-DD" and "YYYY-MM-DDTHH:MM"
        try:
            dt = pd.to_datetime(date, format="%Y-%m-%d")
        except:
            dt = pd.to_datetime(date, errors="coerce")
        day = float(dt.day)
        month = float(dt.month)

        # Numeric inputs
        minTemp = float(request.form['mintemp'])
        maxTemp = float(request.form['maxtemp'])
        rainfall = float(request.form['rainfall'])
        evaporation = float(request.form['evaporation'])
        sunshine = float(request.form['sunshine'])
        windGustSpeed = float(request.form['windgustspeed'])
        windSpeed9am = float(request.form['windspeed9am'])
        windSpeed3pm = float(request.form['windspeed3pm'])
        humidity9am = float(request.form['humidity9am'])
        humidity3pm = float(request.form['humidity3pm'])
        pressure9am = float(request.form['pressure9am'])
        pressure3pm = float(request.form['pressure3pm'])
        temp9am = float(request.form['temp9am'])
        temp3pm = float(request.form['temp3pm'])
        cloud9am = float(request.form['cloud9am'])
        cloud3pm = float(request.form['cloud3pm'])
        location = float(request.form['location'])
        windDir9am = float(request.form['winddir9am'])
        windDir3pm = float(request.form['winddir3pm'])
        windGustDir = float(request.form['windgustdir'])
        rainToday = float(request.form['raintoday'])

        # Arrange features in correct order
        input_lst = [
            location, minTemp, maxTemp, rainfall, evaporation, sunshine,
            windGustDir, windGustSpeed, windDir9am, windDir3pm,
            windSpeed9am, windSpeed3pm, humidity9am, humidity3pm,
            pressure9am, pressure3pm, cloud9am, cloud3pm,
            temp9am, temp3pm, rainToday, month, day
        ]

        # Ensure 2D array
        pred = model.predict([input_lst])[0]

        if pred == 0:
            return render_template("after_sunny.html")
        else:
            return render_template("after_rainy.html")

    return render_template("predictor.html")

if __name__ == '__main__':
    app.run(debug=True,port=0)  
