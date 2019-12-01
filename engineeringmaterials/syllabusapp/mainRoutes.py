from syllabusapp import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/r10')
def r10():
	return render_template("r10.html")

@app.route('/r13')
def r13():
	return render_template("r13.html")

@app.route('/r16')
def r16():
	return render_template("r16.html")

@app.route('/r19')
def r19():
	return render_template("r19.html")