from flask import (
	Flask,
	redirect,
	render_template,
)
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/blogging')
def blogging():
	return redirect('https://micapie.com')

@app.route('/coding')
def coding():
	return redirect('https://github.com/micaswyers')

@app.route('/oninstagram')
def oninstagram():
	return redirect('https://www.instagram.com/micaswyers')

@app.route('/tweeting')
def tweeting():
	return redirect('https://twitter.com/micaswyers')

if __name__ == "__main__":
	app.run(host='0.0.0.0')
