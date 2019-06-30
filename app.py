from flask import Flask
from flask_restful import Resource, Api, reqparse

books = [
    {
        "title": "Harry Potter",
        "price": 15.99,
    },
    {
        "title": "Lord of the Rings",
        "price": 49.99
    },
]

app = Flask(__name__)
api = Api(app)


class Booklist(Resource):
    def get(self):
        return {'books': books}  # default status_code is 200


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, title):
        for book in books:
            if book['title'] == title:
                return {'book': book}
        return {'message': 'No such book found'}, 404

    def post(self, title):
        for book in books:
            if book['title'] == title:
                return {'message': f'Book {title} already exists'}, 400
        data = Book.parser.parse_args()
        item = {'title': title, 'price': data['price']}
        books.append(item)
        return {'book': item}, 201

    def put(self, title):
        for i in range(len(books)):
            if books[i]['title']== title:
                data = Book.parser.parse_args()
                books[i]['price'] = data['price']
                return {'book': books[i]}, 200
        return {'message': f'Book {title} not found.'}, 404

    def delete(self, title):
        for i in range(len(books)):
            if books[i]['title']== title:
                del books[i]
                return {'message': f'Book {title} deleted'}, 200
        return {'message': f'Book {title} not found.'}, 404


api.add_resource(Booklist, '/books')
api.add_resource(Book, '/book/<string:title>')

if __name__ == '__main__':
    app.run(debug=True)
