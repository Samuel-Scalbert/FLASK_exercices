from ..app import app, db, login
from flask import render_template, request, flash, redirect, url_for
from ..models.factbook import Country, Resources, Map
from ..models.formulaires import InsertionPays, InsertionResource, InsertionUser, Connexion
from ..models.users import Users
from ..utils.transformations import  clean_arg
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/insertions/pays", methods=['GET', 'POST'])
@login_required
def insertion_pays():
    form = InsertionPays() 

    try:
        if form.validate_on_submit():
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            code_pays =  clean_arg(request.form.get("code_pays", None))
            type =  clean_arg(request.form.get("type", None))
            introduction =  clean_arg(request.form.get("introduction", None))
            ressources =  clean_arg(request.form.getlist("ressources", None))
            continent =  clean_arg(request.form.get("continent", None))

            nouveau_pays = Country(id=code_pays, 
                Introduction=introduction,
                name=nom_pays,
                type = type)

            for ressource in ressources:
                ressource = Resources.\
                    query.\
                    filter(Resources.id == ressource).\
                    first()
                nouveau_pays.resources.append(ressource)
            
            nouveau_pays.maps.append(Map.query.filter(Map.name==continent).first())

            db.session.add(nouveau_pays)
            db.session.commit()
    
    except Exception as e :
        print(e)
    
    return render_template("pages/insertion_pays.html", 
            sous_titre= "Insertion pays" , 
            form=form)

@app.route("/insertions/ressource", methods=['GET', 'POST'])
def ressources():
    form = InsertionPays()

    try:
        if form.validate_on_submit():
            ressources = clean_arg(request.form.getlist("ressources", None))

            nouvelle_ressource = Resources(ressources=ressources)

            for ressource in ressources:
                ressource = Resources. \
                    query. \
                    filter(Resources.id == ressource). \
                    first()
                nouvelle_ressource.resources.append(ressource)

            nouvelle_ressource.maps.append(Map.query.filter(Map.name == continent).first())

            db.session.add(nouvelle_ressource)
            db.session.commit()

    except Exception as e:
        print(e)

    return render_template("pages/insertion_ressource.html",
                           sous_titre="Insertion Ressource",
                           form=form)

@app.route("/insertions/utilisateur", methods=["GET", "POST"])
def insertion_user():
    form = InsertionUser()

    if form.validate_on_submit():
        statut, donnees = Users.ajout(
            prenom=clean_arg(request.form.get("prenom", None)),
            password=clean_arg(request.form.get("password", None))
        )
        if statut is True:
            flash("Ajout effectué", "success")
            return redirect(url_for("insertion_user"))
        else:
            flash(",".join(donnees), "error")
            return render_template("pages/ajout_utilisateur.html", form=form)
    else:
        return render_template("pages/ajout_utilisateur.html", form=form)

@app.route("/utilisateurs/connexion", methods=["GET", "POST"])
def connexion():
    form = Connexion()

    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté", "info")
        return redirect(url_for("pays"))

    if form.validate_on_submit():
        utilisateur = Users.identification(
            prenom=clean_arg(request.form.get("prenom", None)),
            password=clean_arg(request.form.get("password", None))
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect(url_for("pays"))
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")
            return render_template("pages/connexion.html", form=form)

    else:
        return render_template("pages/connexion.html", form=form)

login.login_view = 'connexion'

@app.route("/utilisateurs/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté", "info")
    return redirect(url_for("pays"))