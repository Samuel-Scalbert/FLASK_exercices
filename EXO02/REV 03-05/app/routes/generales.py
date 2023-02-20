from ..app import app
from flask import render_template
import json

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

@app.route("/parcs_eoliens")
def eolien():
    f = open('app/routes/installations-de-production-eolien-par-commune.json')
    data = json.load(f)
    return render_template("pages/pays.html", data=data)

@app.route("/parc_specifique/<string:id>")
def parc_specifique(id):
    f = open('app/routes/installations-de-production-eolien-par-commune.json')
    data = json.load(f)
    for parc in data:
        if int(parc.get("code_epci")) == int(id):
            return render_template("pages/parc.html", parc=parc)
    return "pas de parc"