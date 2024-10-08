from flask import Flask, render_template, url_for

app = Flask(__name__)


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
    app.run(debug=False)