from syllabusapp import app
from flask import render_template

@app.route('/r13cse')
def r13cse():
	return render_template("r13/r13cse.html")

@app.route('/r13it')
def r13it():
	return render_template("r13/r13it.html")

@app.route('/r13ece')
def r13ece():
	return render_template("r13/r13ece.html")

@app.route('/r13eee')
def r13eee():
	return render_template("r13/r13eee.html")

@app.route('/r13mech')
def r13mech():
	return render_template("r13/r13mech.html")

@app.route('/r13civil')
def r13civil():
	return render_template("r13/r13civil.html")

@app.route('/r13pet')
def r13pet():
	return render_template("r13/r13pet.html")

@app.route('/r13mine')
def r13mine():
	return render_template("r13/r13mine.html")

@app.route('/r13agri')
def r13agri():
	return render_template("r13/r13agri.html")


