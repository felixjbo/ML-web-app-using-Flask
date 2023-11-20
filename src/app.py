from flask import Flask, request, render_template
from pickle import load
import pandas as pd

app = Flask(__name__)
model = load(open("../models/relu_adam_42.pkl", "rb"))

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        HighBP = float(request.form["HighBP"])
        HighChol = str(request.form["HighChol"])
        BMI = str(request.form["BMI"])
        Smoker = str(request.form["Smoker"])
        Stroke = float(request.form["Stroke"])
        Diabetes = float(request.form["Diabetes"])
        PhysActivity = float(request.form["PhysActivity"])
        HvyAlcoholConsump = float(request.form["HvyAlcoholConsump"])
        Sex = float(request.form["Sex"])
        colums = ['HighBP','HighChol','BMI','Smoker','Stroke','Diabetes','PhysActivity','HvyAlcoholConsump','Sex']

        data = pd.DataFrame([[HighBP, HighChol, BMI, Smoker, Stroke, Diabetes, PhysActivity, HvyAlcoholConsump, Sex]], columns=colums)
        print(data)
        prediction = str(model.predict(data)[0])
        print(prediction)
    else:
        prediction = None
    
    return render_template("index.html", prediction = prediction)