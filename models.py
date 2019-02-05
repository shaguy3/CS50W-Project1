from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm, LoginForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '67fbe61600452e3f1a211569e15aec78'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def import_books():
	db.create_all()
	with open('books.csv', 'r') as csv_file:
		line_count = 1
		csv_reader = csv.reader(csv_file, delimiter=',')
		for line in csv_reader:
			if line_count == 1:
				line_count += 1
			else:
				book = Book(isbn=str(line[0]), title=str(line[1]), author=str(line[2]), publish_year=int(line[3]))
				db.session.add(book)
				line_count += 1
		db.session.commit()


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
	isbn = db.Column(db.String(60), primary_key=True)
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


if __name__ == '__main__':
	import_books()