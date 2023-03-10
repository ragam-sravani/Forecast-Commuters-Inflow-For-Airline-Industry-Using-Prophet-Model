import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import os
model=pickle.load(open("D:\major\Forecast Commuters Inflow For Airline Industry IBM Cloud Services\Flask\Airlines-prophet-1.pkl",'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["Date"]
        a={"ds":[ds]}
        ds=pd.DataFrame(a)
        prediction = model.predict(ds)
        print(prediction)
        output=round(prediction.iloc[0,15])
        print(output)
        return render_template('home.html',prediction_text="Commuters Inflow on selected date is. {} thousands".format(output))
    return render_template("home.html")

    
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
