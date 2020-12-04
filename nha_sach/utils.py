import json, hashlib
from nha_sach.models import User, UserRole, Book
from nha_sach import db

def read_data(path='data/typeOfBook.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def read_books(typebook_id=None, kw=None, from_price=None, to_price=None):
    books = Book.query

    if typebook_id:
        books = books.filter(Book.typeofbook_id == typebook_id)

    if kw:
        books = books.filter(Book.name.contains(kw))

    if from_price and to_price:
        books = books.filter(Book.price.__gt__(from_price),
                             Book.price.__lt__(to_price))

    return books.all()
    # books = read_data(path='data/book.json')
    #
    # if book_id:
    #     cate_id = int(book_id)
    #     books = [p for p in books
    #                 if p['typeofbook_id'] == book_id]
    #
    # if kw:
    #     books = [p for p in books
    #                 if p['name'].find(kw) >= 0]
    #
    # if from_price and to_price:
    #     from_price = float(from_price)
    #     to_price = float(to_price)
    #     books = [p for p in books
    #                 if to_price >= p['price'] >= from_price]
    #
    # return books


def get_book_by_id(book_id):
    return Book.query.get(book_id)
    # books = read_data('data/book.json')
    # for p in books:
    #     if p['id'] == book_id:
    #         return p


def check_login(username, password, role = UserRole.ADMIN):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    user = User.query.filter(User.username == username.strip(),
                             User.password == password,
                             User.user_role == role).first()
    return user


def add_user(name, email, username, password, avatar_path):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, email=email,
             username=username, password=password,
             avatar=avatar_path)
    try:
        db.session.add(u)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False
    
    
def get_user_by_id(user_id):
   return User.query.get(user_id)