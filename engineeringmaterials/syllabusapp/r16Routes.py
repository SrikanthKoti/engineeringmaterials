from syllabusapp import app
from flask import render_template

@app.route('/r16cse')
def r16cse():
	return render_template("r16/r16cse.html")

@app.route('/r16it')
def r16it():
	return render_template("r16/r16it.html")

@app.route('/r16ece')
def r16ece():
	return render_template("r16/r16ece.html")

@app.route('/r16eee')
def r16eee():
	return render_template("r16/r16eee.html")

@app.route('/r16mech')
def r16mech():
	return render_template("r16/r16mech.html")

@app.route('/r16civil')
def r16civil():
	return render_template("r16/r16civil.html")

@app.route('/r16pet')
def r16pet():
	return render_template("r16/r16pet.html")

@app.route('/r16mine')
def r16mine():
	return render_template("r16/r16mine.html")

@app.route('/r16agri')
def r16agri():
	return render_template("r16/r16agri.html")


