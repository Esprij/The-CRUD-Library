# import sqlite3
#
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (
#                   id INTEGER PRIMARY KEY,
#                   title varchar(250) NOT NULL UNIQUE, "
#                  "author varchar(250) NOT NULL,
#                   rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Create the extension
db = SQLAlchemy()
# Initialize the app with the extension
db.init_app(app)


# Books TABLE Configuration
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()

# Notice how the query is inside app.app_context(), this is needed for whatever modifications are going to be made
# to a database
# CREATES data
with app.app_context():

    book = Book(
        id=1,
        title="Harry Potter and the Goblet of Fire",
        author="J. K. Rowling",
        rating="9.3"
    )
    # Query to add an entry
    db.session.add(book)
    db.session.commit()


# PRACTICING CRUD OPERATIONS

# READ all data from a db
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars().all()
#
#     for book in all_books:
#         print(f"{book.title} - {book.author} - {book.rating}/10")

# READ specific data from a db
# book_id = 1
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#
#     print(book)

# UPDATE data from a db through title, id, or any attribute you'd like
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
#     book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     print(book)

# DELETE data from a db through title, id or any other special/specific attribute
# book_id = 1
# with app.app_context():
#     book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
