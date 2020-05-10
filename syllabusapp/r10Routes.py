from syllabusapp import app
from flask import render_template

@app.route('/r10cse')
def r10cse():
	return render_template("r10/r10cse.html")

@app.route('/r10it')
def r10it():
	return render_template("r10/r10it.html")

@app.route('/r10ece')
def r10ece():
	return render_template("r10/r10ece.html")

@app.route('/r10eee')
def r10eee():
	return render_template("r10/r10eee.html")

@app.route('/r10mech')
def r10mech():
	return render_template("r10/r10mech.html")

@app.route('/r10civil')
def r10civil():
	return render_template("r10/r10civil.html")

@app.route('/r10pet')
def r10pet():
	return render_template("r10/r10pet.html")

@app.route('/r10mine')
def r10mine():
	return render_template("r10/r10mine.html")

@app.route('/r10agri')
def r10agri():
	return render_template("r10/r10agri.html")


