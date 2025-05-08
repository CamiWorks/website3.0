import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
@app.route('/ ') # assigning multiple paths to the same index
def index():
    # adding a html template 
    return render_template('index-5.html')

# Prtfolio
@app.route('/portfolio')
def portfolio():
    return render_template('work-1.html')

# Works 
@app.route('/realGenie')
def realGenie():
    return render_template('work-2.html')

@app.route('/latinArte')
def latinArte():
    return render_template('portfolio-5.html')

@app.route('/mda')
def mda():
    return render_template('portfolio-4.html')

@app.route('/tick')
def tick():
    return render_template('portfolio-1.html')

# Turn on the debuger all the time you run it on pytohn 
if __name__ == '__main__':
    app.run(debug=True)