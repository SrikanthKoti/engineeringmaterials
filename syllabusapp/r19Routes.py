from syllabusapp import app
from flask import render_template

@app.route('/r19cse')
def r19cse():
	return render_template("r19/r19cse.html")

@app.route('/r19it')
def r19it():
	return render_template("r19/r19it.html")

@app.route('/r19ece')
def r19ece():
	return render_template("r19/r19ece.html")

@app.route('/r19eee')
def r19eee():
	return render_template("r19/r19eee.html")

@app.route('/r19mech')
def r19mech():
	return render_template("r19/r19mech.html")

@app.route('/r19civil')
def r19civil():
	return render_template("r19/r19civil.html")

@app.route('/r19pet')
def r19pet():
	return render_template("r19/r19pet.html")

@app.route('/r19mine')
def r19mine():
	return render_template("r19/r19mine.html")

@app.route('/r19agri')
def r19agri():
	return render_template("r10/r10agri.html")


