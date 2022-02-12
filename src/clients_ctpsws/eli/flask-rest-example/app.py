from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import constants
import messages

API_VERSION = "/v1"
BASE_URL = API_VERSION + "/api/"

app = Flask(__name__)

local_db_url = (
    "mysql+pymysql://"
    + constants.USERNAME
    + ":"
    + constants.PASSWORD
    + "@"
    + constants.HOST
    + "/"
    + constants.DB_NAME
)
app.config["SQLALCHEMY_DATABASE_URI"] = local_db_url
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(45), nullable=False)
    author_name = db.Column(db.String(45), nullable=True)
    book_description = db.Column(db.String(100), nullable=True)

    def __init__(self, book_name, author_name, book_description):
        self.book_name = book_name
        self.author_name = author_name
        self.book_description = book_description


@app.route(BASE_URL + "book/create", methods=["POST"])
def createBook():
    status = 500
    message = messages.INTERNAL_SERVER_ERROR

    try:
        data = request.get_json()
        if "book_name" not in data or not data["book_name"]:
            message = "Book name is required"
            status = 400
            return jsonify({"message": message}), status

        book_name = data["book_name"]
        author_name = data["author_name"]
        book_description = data["book_description"]
        book = Book(
            book_name=book_name,
            author_name=author_name,
            book_description=book_description,
        )
        db.session.add(book)
        db.session.commit()
        message = messages.SUCCESS
        status = 200
    except Exception as error:
        db.session.rollback()
        print(error)
    return jsonify({"message": message}), status


@app.route(BASE_URL + "book/all", methods=["GET"])
def getAll():
    status = 500
    message = messages.INTERNAL_SERVER_ERROR

    try:
        books = Book.query.all()
        arr = []
        for a in books:
            book = {}
            book["id"] = a.id
            book["book_name"] = a.book_name
            book["author_name"] = a.author_name
            book["book_description"] = a.book_description
            arr.append(book)
        return jsonify({"books": arr}), 200
    except Exception as error:
        print(error)
        message = error
    return jsonify({"message": message}), status


@app.route(BASE_URL + "book/update", methods=["PUT"])
def updateBook():
    status = 500
    message = messages.INTERNAL_SERVER_ERROR

    try:
        data = request.get_json()
        if "id" not in data or not data["id"]:
            message = "Book not found"
            status = 400
            return jsonify({"message": message}), status

        if "book_name" not in data or not data["book_name"]:
            message = "Book name is required"
            status = 400
            return jsonify({"message": message}), status

        aBook = getBookById(data["id"])
        if aBook is None:
            message = messages.NOT_FOUND
            status = 400
            return jsonify({"message": message}), status
        else:
            aBook.book_name = data["book_name"]
            aBook.author_name = data["author_name"]
            aBook.book_description = data["book_description"]
            db.session.commit()
            message = messages.UPDATE
            status = 200
            return jsonify({"message": message}), status
    except Exception as error:
        db.session.rollback()
        print(error)
    return jsonify({"message": message}), status


@app.route(BASE_URL + "book/<id>", methods=["GET"])
def getById(id):
    status = 500
    message = messages.INTERNAL_SERVER_ERROR

    try:
        aBook = getBookById(id)
        if aBook is None:
            message = messages.NOT_FOUND
            status = 400
            return jsonify({"message": message}), status

        book = {}
        book["id"] = aBook.id
        book["book_name"] = aBook.book_name
        book["author_name"] = aBook.author_name
        book["book_description"] = aBook.book_description
        return jsonify(book), 200

    except Exception as error:
        print(error)
        message = error
    return jsonify({"message": message}), status


@app.route(BASE_URL + "book/<id>", methods=["DELETE"])
def deleteBook(id):
    status = 500
    message = messages.INTERNAL_SERVER_ERROR

    try:
        aBook = getBookById(id)
        if aBook is None:
            message = messages.NOT_FOUND
            status = 400
            return jsonify({"message": message}), status

        db.session.delete(aBook)
        db.session.commit()
        message = messages.DELETE
        status = 200
        return jsonify({"message": message}), status
    except Exception as error:
        db.session.rollback()
        print(error)
        message = error
    return jsonify({"message": message}), status


def getBookById(id):
    try:
        book = Book.query.filter_by(id=id).first()
        return book
    except Exception as error:
        print(error)
        return None


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
