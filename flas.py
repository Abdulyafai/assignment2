from flask import Flask, redirect, url_for, render_template, request
from assignment2 import bodymass
from assignment2 import retirement

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cal", methods=["POST", "GET"])
def cal():
    if request.method == "POST":
        weight = request.form["bodymass"]
        height = request.form["height"]
        total = bodymass(float(weight), float(height))
        return redirect(url_for("resul", res=total))
    else:
        return render_template("index.html")

@app.route("/calr", methods=["POST", "GET"])
def calr():
    if request.method == "POST":
        age = request.form["age"]
        salay = request.form["Salary"]
        perc = request.form["Percentage"]
        goal = request.form["goal"]
        total = retirement(int(age), float(salay), int(perc), float(goal))
        return redirect(url_for("resulr", resr=total))
    else:
        return render_template("index.html")

@app.route("/<res>")
def resul(res):
    return f"<h2>your body mass is: {res}</h2>"

@app.route("/<resr>")
def resulr(resr):
    return f"<h2>You are meeting your goal on: {res} years old</h2>"

if __name__ == "__main__":
    app.run(debug=True)
