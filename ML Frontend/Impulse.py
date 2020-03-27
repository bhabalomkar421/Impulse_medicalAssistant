from flask import Flask, render_template, request, url_for, send_file, flash, redirect
import pickle
import numpy as np
import os
import json

import CurrentStats
import CancerModel
import PdfConverter
from PdfConverter import PDFPageCountError

# import warnings

app = Flask(__name__)
app.config['SECRET_KEY'] = '73a4b6ca8cb647a20b71423e31492452'

# For Coronavirus
with open("Models\Coronavirus_logistic", "rb") as f:
    logisticRegression = pickle.load(f)


# For Chronic kidney disease
with open("Models\CKD_Model", "rb") as f:
    decisionTree = pickle.load(f)


@app.route("/")
@app.route("/home")
def Homepage():
    cases, cured, death = CurrentStats.currentStatus()
    return render_template("Homepage.html", cases=cases, cured=cured, death=death)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("PageNotFound.html")


@app.route("/currentstats", methods=["POST", "GET"])
def CurrentStatus():
    cases, cured, death = CurrentStats.currentStatus()
    scases = scured = sdeath = 0
    state = ""
    try:
        if request.method == "POST":
            # print(request.form)
            formDict = request.form
            state = formDict['state']
            scases, scured, sdeath = CurrentStats.StateStatus(state)
    except UnboundLocalError:
        flash("The State is not Effected Yet")
    return render_template("CurrentStats.html", state=state, scases=scases, scured=scured, sdeath=sdeath, cases=cases, cured=cured, death=death, title="Current Statistics", navTitle="Current Status", headText="Caronavirus Current Stats Statewise", ImagePath="/static/Virus.png")


@app.route("/about")
def About():
    return render_template("About.html")


@app.route("/contact")
def Contact():
    return render_template("Contact.html")


@app.route("/infected")
def Infected():
    return render_template("Infected.htm", disease="Nothing")


@app.route("/noninfected")
def NonInfected():
    return render_template("NonInfected.htm")


@app.route("/download")
def Download():
    file = "static/Example.docx"
    return send_file(file, as_attachment=True)


@app.route("/BreastCancer", methods=["POST", "GET"])
def BreastCancer():
    if request.method == "POST":
        f = request.files['inputFile']

        name, extension = os.path.splitext(f.filename)
        print(extension)
        try:
            if extension == ".png" or extension == ".jpg" or extension == ".jpeg" or extension == ".pdf":
                location = os.path.join("Received_Files", f.filename)
                f.save(location)
                print("File Saved !")
                if extension == ".pdf":
                    PdfConverter.Convert(f.filename)
                    image = name + ".png"
                    prediction = CancerModel.Predict(
                        os.path.join("Received_Files", image))
                else:
                    prediction = CancerModel.Predict(
                        os.path.join("Received_Files", f.filename))
                print(prediction)
                if prediction:
                    return render_template("Infected.htm", disease="Breast Cancer ")
                else:
                    return render_template("NonInfected.htm")

            else:
                flash(
                    "Please upload files with extension 'png', 'pdf' , 'jpg' or 'jpeg'")

        except ValueError:
            flash("Please Upload Only Valid Files ")
        except PDFPageCountError:
            flash("Please Upload Only Valid Files , or try again later")
    return render_template("BreastCancer.html", title="Breast Cancer", navTitle="Breast Cancer", headText="Breast Cancer Probability Detector", ImagePath="/static/BreastCancer.jpg")


@app.route("/HeartDisease", methods=["POST", "GET"])
def Heart_disease():
    return render_template("HeartDisease.html", title="Heart Disease Detector", navTitle="Heart Disease Detector", headText="Heart Disease Probabilty Detector", ImagePath="/static/HeartPulse.png")


# @app.route("/test", methods=["POST", "GET"])
# def test():
#     if request.method == "POST"
    # data_dic = json.loads(data)
    # print(data_dic.keys())


@app.route("/DiseasePrediction", methods=["POST", "GET"])
def DiseasePrediction():
    if request.method == "POST":
        print(request.form)
        # data_dic = json.loads(data)
        # print(data_dic.keys())
    return render_template("DiseasePrediction.html")


@app.route("/CKD", methods=["POST", "GET"])
def CKD():
    if request.method == "POST":
        submitted_values = request.form
        sg = str(float(submitted_values["sg"].strip()))
        albumin = str(float(submitted_values["albumin"].strip()))
        hemoglobin = str(float(submitted_values["hemoglobin"].strip()))
        pcv = str(float(submitted_values["pcv"].strip()))
        hypertension = str(float(submitted_values["hypertension"].strip()))
        sc = str(float(submitted_values["sc"].strip()))

        ckd_inputs1 = [sg, albumin, sc, hemoglobin, pcv, hypertension]
        prediction = decisionTree.predict([ckd_inputs1])
        # print("**************             ", prediction)
        if not prediction:
            return render_template("Infected.htm", disease="Chronic Kidney Disease")
        else:
            return render_template("NonInfected.htm")

    return render_template("ChronicKidney.html", title="Chronic Kidney Disease", navTitle="Chronic Kidney Disease", headText="Chronic Kidney Disease Detector", ImagePath="/static/Chronic_Kidney.png")


@app.route("/CoronavirusPrediction", methods=["POST", "GET"])
def Coronavirus():
    if request.method == "POST":
        # print(request.form)
        submitted_values = request.form
        temperature = float(submitted_values["temperature"].strip())
        age = int(submitted_values["age"])
        cough = int(submitted_values["cough"])
        cold = int(submitted_values["cold"])
        sore_throat = int(submitted_values["sore_throat"])
        body_pain = int(submitted_values["body_pain"])
        fatigue = int(submitted_values["fatigue"])
        headache = int(submitted_values["headache"])
        diarrhea = int(submitted_values["diarrhea"])
        difficult_breathing = int(submitted_values["difficult_breathing"])
        travelled14 = int(submitted_values["travelled14"])
        travel_covid = int(submitted_values["travel_covid"])
        covid_contact = int(submitted_values["covid_contact"])

        age = 2 if (age > 50 or age < 10) else 0
        temperature = 1 if temperature > 98 else 0
        difficult_breathing = 2 if difficult_breathing else 0
        travelled14 = 3 if travelled14 else 0
        travel_covid = 3 if travel_covid else 0
        covid_contact = 3 if covid_contact else 0

        model_inputs = [cough, cold, diarrhea,
                        sore_throat, body_pain, headache, temperature, difficult_breathing, fatigue, travelled14, travel_covid, covid_contact, age]
        prediction = logisticRegression.predict([model_inputs])[0]
        # print("**************             ", prediction)
        if prediction:
            return render_template("Infected.htm", disease="Coronavirus")
        else:
            return render_template("NonInfected.htm")

    return render_template("Coronavirus.htm", title="Caronavirus Prediction", navTitle="COVID-19 Detector", headText="Coronavirus Probability Detector", ImagePath="/static/VirusImage.png")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=14444, debug=True, threaded=True)
