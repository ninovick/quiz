from flask import Flask, render_template, request
from helpers import favorite, delist

app: Flask = Flask(__name__)

flavor_dict: dict[str, int] = {"Sweet": 0, "Sour": 0, "Spicy": 0, "Salty": 0}
fav_flavs: str = ""

user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/quizpg1', methods=["GET", "POST"])
def quizpg1():
    if request.method == "POST":
        global sweet, sour, spicy, salty  
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1
        return render_template("quizpg2.html")
    return render_template("quizpg1.html")

@app.route('/quizpg2', methods=["GET", "POST"])
def quizpg2():
    if request.method == "POST":
        global sweet, sour, spicy, salty  
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1
        # return render_template("quizpg3.html")
    return render_template("quizpg2.html")

@app.route('/quizpg3', methods=["GET", "POST"])
def quizpg3():
    if request.method == "POST":
        global sweet, sour, spicy, salty  
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1
        # return render_template("quizpg4.html")
    return render_template("quizpg3.html")

@app.route('/quizpg4', methods=["GET", "POST"])
def quizpg4():
    if request.method == "POST":
        global sweet, sour, spicy, salty, fav_flavs 
        flavor = (request.form["image-pick"])
        flavor_dict[flavor] += 1

        fav = favorite(flavor_dict)
        fav_flavs = delist(fav)
    return render_template("quizpg4.html")

@app.route('/results',  methods=["GET", "POST"])
def results():
    global fav_flavs
    return render_template("results.html", fav_flavs=fav_flavs)

if __name__ == '__main__':
    main
    flavor_dict: dict[str, int] = {"Sweet": 0, "Sour": 0, "Spicy": 0, "Salty": 0}
    app.run(debug=True)