from flask import Flask, render_template
from ..app import app

@app.route("/division/<int:nb>/<int:nb_02>")
def page_pays(nb,nb_02):
    nombre = nb / nb_02
    return str(nombre)