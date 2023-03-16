from flask import render_template,request, redirect

from flask_app import app

from flask_app.models import dojo,ninja

@app.route('/ninjas')
def show_ninjas():
    dojos = dojo.Dojo.get_all()
    return render_template("ninja.html", all_dojos = dojos)

@app.route('/add/ninja', methods = ['POST'])
def add_ninja():
    ninja.Ninja.save_ninja(request.form)
    print(request.form)
    return redirect ("/")

@app.route('/ninja/edit/<int:id>/<int:dojo_id>')
def edit_ninja(id, dojo_id):
    db_data = {
        "id":id,
        "dojos_id":dojo_id
    }
    return render_template ("edit_ninja.html", one_ninja = ninja.Ninja.get_one(db_data))

@app.route('/ninja/update/<int:id>/<int:dojo_id>', methods = ['POST'])
def update_ninja(id, dojo_id):
    db_data = {
        "id": id,
        "first_name": request.form ['first_name'],
        "last_name": request.form ['last_name'],
        "age": request.form['age'], 
        "dojos_id": dojo_id
    }
    ninja.Ninja.update(db_data)
    return redirect (f"/dojos/show/{dojo_id}")