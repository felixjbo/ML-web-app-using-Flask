from pickle import load
from flask import Flask, request, render_template

app = Flask(__name__)
model = load(open("/workspaces/ML-web-app-using-Flask/models/NLP_default_42.sav", "rb"))
class_dict = {
    "0": "Not Spam",
    "1": "Spam"
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        
        data = [[val1]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)