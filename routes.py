from flask import Blueprint, jsonify, request, make_response
from models import db, Book

book_blueprint = Blueprint(
    "book_api_routes", __name__, url_prefix="/api/v1/book"
)


@book_blueprint.route("/", methods=["GET"])
def all_books():
    books = Book.query.all()
    serialized_books = [b.serialize() for b in books]
    response = {
        "message": "Returning all books",
        "result": serialized_books
    }
    return make_response(
        jsonify(response)
    )


@book_blueprint.route("/", methods=["POST"])
def create_book():
    try:

        book = Book()
        book.name = request.form["name"]
        book.slug = request.form["slug"]
        book.image = request.form["image"]
        book.author = request.form["author"]
        book.price = request.form["price"]

        db.session.add(book)
        db.session.commit()

        response = {
            "message": "Book created",
            "book": book.serialize()
        }
    except Exception as e:
        print(str(e))
        response = {
            "message": "Fail to create book",
        }

    return make_response(jsonify(response))


@book_blueprint.route("/<slug>", methods=["GET"])
def book_details(slug):
    book = Book.query.filter_by(slug=slug).first()
    if book:
        return make_response(jsonify({
            "book": book.serialize()
        }), 200)

    return make_response(jsonify({
        "message": "This book does not exists"
    }), 404)
