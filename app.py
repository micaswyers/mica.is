from flask import (
	Flask,
	redirect,
	render_template,
)
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/tweeting')
def tweeting():
	return redirect('https://twitter.com/micaswyers')

@app.route('/blogging')
def blogging():
	return redirect('https://micapie.com')
