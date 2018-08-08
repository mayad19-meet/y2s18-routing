from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

#@app.route('/home.html')
#def home():
 #   return render_template(
  #  	'home.html')
@app.route('/<int:student_id>')
def display_student(student_id):
	return render_template('student.html',s=student_id)     
@app.route('/')
def home_route():
	return render_template('home.html')
app.run(debug=True)
