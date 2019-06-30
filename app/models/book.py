from app import db


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def json(self):
        return {'title': self.title, 'price': self.price}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
