from flask import render_template, url_for, flash, redirect
from imdBooks.models import User, Book, Review
from imdBooks.forms import RegisterationForm, LoginForm
from imdBooks import app

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
