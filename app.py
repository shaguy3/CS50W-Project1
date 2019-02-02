from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('home.html', title='home')

@app.route("/about")
def about_page():
	return render_template('about.html', title='about')

if __name__ == '__main__':
	app.run(debug=True)
