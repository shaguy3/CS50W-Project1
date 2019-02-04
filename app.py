from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '67fbe61600452e3f1a211569e15aec78'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	reviews = db.relationship('Review', backref='reviewer', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Book(db.Model):
	isbn = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60), nullable=False)
	author = db.Column(db.String(60), nullable=False, default='Unknown')
	publish_year = db.Column(db.Integer, nullable=False, default='Unknown')
	book_reviews = db.relationship('Review', backref='reviewed book', lazy=True)

	def __repr__(self):
		return f"Book('{self.title}', '{self.author}', '{self.publish_year}')"


class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), nullable=False)
	reviewing_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	review_score = db.Column(db.Integer, nullable=False)
	review_text = db.Column(db.Text)

	def __repr__(self):
		return f"Review('{self.book_isbn}', '{self.reviewing_user}', '{self.review_score}')"


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
