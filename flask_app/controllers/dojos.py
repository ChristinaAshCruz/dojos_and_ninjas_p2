from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos = dojos)


@app.route('/dojos/new')
def add_dojo():
    return redirect("dojo.html")

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect ("/")

@app.route('/dojos/show/<int:id>')
def show_dojo(id):
    db_data = {
        "id": id
    }
    return render_template("dojo_show.html", dojo=Dojo.get_one(db_data))

# @app.route('/ninja/edit/<int:id>')
# def edit_ninja(id):
#     db_data = {
#         "id":id
#     }
#     return render_template ("edit_ninja.html", one_ninja = Dojo.get_one(db_data))