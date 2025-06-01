from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
class Base(DeclarativeBase):
  pass
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Book(title="Harry Potter", author="J.K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

@app.route("/")
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form["name"]
        book_author = request.form["author"]
        book_rating = request.form["rating"]

        new_book = Book(title=book_name, author=book_author, rating=book_rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["POST"])
def update_rating(book_id):
    new_rating = request.form.get('new_rating')
    book_to_update = db.session.query(Book).get(book_id)
    if book_to_update:
        book_to_update.rating = float(new_rating)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    book_to_delete = db.session.query(Book).get(book_id)
    if book_to_delete:
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

