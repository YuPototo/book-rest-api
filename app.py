from flask import Flask, jsonify, request

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


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({
        "books": books
    })


@app.route('/book/<string:title>', methods=['GET'])
def get_book(title):
    for book in books:
        if book['title'] == title:
            return jsonify({
                'book': book
            })
    return jsonify({'message': 'No such books'})


@app.route('/book/<string:title>', methods=['POST'])
def create_book(title):
    for book in books:
        if title == book['title']:
            return jsonify({
                'message': 'book already exists'
            })
    request_data = request.get_json()
    new_book = {
        'title': title,
        'price': request_data['price']
    }
    books.append(new_book)
    return jsonify(new_book)


@app.route('/book/<string:title>', methods=['PUT'])
def update_book(title):
    for i in range(len(books)):
        if books[i]['title'] == title:
            request_data = request.get_json()
            updated_book = {
                'title': title,
                'price': request_data['price']
            }
            books[i] = updated_book
            return jsonify(updated_book)
    return jsonify({'message': 'No such book found'})


@app.route('/book/<string:title>', methods=['DELETE'])
def delete_book(title):
    for i in range(len(books)):
        if books[i]['title'] == title:
            del books[i]
        return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book no found'})


if __name__ == '__main__':
    app.run(debug=True)
