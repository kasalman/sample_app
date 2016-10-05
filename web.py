from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('sample_page.html')

@app.route('/about')
def second():
	return render_template('about.html')

app.run(debug=True)