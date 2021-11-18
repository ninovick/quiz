from flask import Flask, render_template, request
from helpers import favorite, delist

app: Flask = Flask(__name__)

flavor_dict: dict[str, int] = {"Sweet": 0, "Sour": 0, "Spicy": 0, "Salty": 0}
fav_flavs: str = ""

user_number: int = 0

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/quizpg1', methods=["GET", "POST"])
def quizpg1():
    return render_template("quizpg1.html")

@app.route('/quizpg2', methods=["GET", "POST"])
def quizpg2():
    if request.method == "POST":
        global flavor_dict 
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1
    return render_template("quizpg2.html")

@app.route('/quizpg3', methods=["GET", "POST"])
def quizpg3():
    if request.method == "POST":
        global flavor_dict
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1
    return render_template("quizpg3.html")

@app.route('/quizpg4', methods=["GET", "POST"])
def quizpg4():
    if request.method == "POST":
        global flavor_dict
        flavor = (request.form["image-pick"])  
        flavor_dict[flavor] += 1
    return render_template("quizpg4.html")

@app.route('/results',  methods=["GET", "POST"])
def results():
    global fav_flavs, flavor_dict
    if request.method == "POST":
        global flavor_dict  
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1
        fav = favorite(flavor_dict)
        fav_flavs = delist(fav)
    flavor_dict = {"Sweet": 0, "Sour": 0, "Spicy": 0, "Salty": 0}
    return render_template("results.html", fav_flavs=fav_flavs)

if __name__ == '__main__':
    app.run(debug=True)

