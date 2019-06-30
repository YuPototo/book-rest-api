from flask_restful import Resource, reqparse
from models.book import BookModel


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, title):
        book = BookModel.find_by_title(title)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    def post(self, title):
        if BookModel.find_by_title(title):
            return {'message': 'Book already exists'}, 400
        data = Book.parser.parse_args()
        book = BookModel(title=title, **data)

        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return book.json(), 201

    def put(self, title):
        data = Book.parser.parse_args()

        book = BookModel.find_by_title(title)

        if book:
            book.price = data['price']
        else:
            book = BookModel(title, **data)

        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return book.json()

    def delete(self, title):
        book = BookModel.find_by_title(title)
        if book:
            book.delete_from_db()
            return {'message': 'Book deleted.'}
        return {'message': 'Book not found.'}, 404


class Booklist(Resource):
    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}
