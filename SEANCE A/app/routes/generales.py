from ..app import app
from flask import render_template
from ..app import app,db
from sqlalchemy import text
from ..models.factbook import Country, Aera, Map
import json

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

@app.route("/pays")
def pays():
    pays = Country.query.all()
    return render_template("pages/pays.html", data = pays)
