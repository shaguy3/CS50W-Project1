from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '67fbe61600452e3f1a211569e15aec78'

@app.route('/')
def home():
	return render_template('home.html', title='home')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
	app.run(debug=True)
