import json, hashlib
from nha_sach.models import User, UserRole, Book, Customer, Receipt, ReceiptDetail
from nha_sach import db
from flask_login import current_user

def read_data(path='data/typeOfBook.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def read_books(tpbook_id=None, kw=None, from_price=None, to_price=None):
    books = Book.query

    if tpbook_id:
        books = books.filter(Book.typeofbook_id == tpbook_id)

    if kw:
        books = books.filter(Book.name.contains(kw))

    if from_price and to_price:
        books = books.filter(Book.price.__gt__(from_price),
                             Book.price.__lt__(to_price))

    return books.all()
    # books = read_data(path='data/books.json')
    #
    # if tpbook_id:
    #     tpbook_id = int(tpbook_id)
    #     books = [p for p in books
    #              if p['typeofbook_id'] == tpbook_id]
    #
    # if kw:
    #     books = [p for p in books
    #              if p['name'].find(kw) >= 0]
    #
    # if from_price and to_price:
    #     from_price = float(from_price)
    #     to_price = float(to_price)
    #     books = [p for p in books
    #             if to_price >= p['price'] >= from_price]
    #
    # return books


def get_book_by_id(book_id):
    return Book.query.get(book_id)
    # books = read_data('data/books.json')
    # for p in books:
    #     if p['id'] == book_id:
    #         return p


def check_login(username, password, role = UserRole.ADMIN):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    user = User.query.filter(User.username == username.strip(),
                             User.password == password,
                             User.user_role == role).first()
    return user



def add_user(name, phone, email, username, password, gender, avatar_path):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = Customer(name=name, email=email, phone=phone,
             username=username, password=password, gender=gender,
             avatar=avatar_path)
    y = User(name=name, email=email,
             username=username, password=password, gender=gender,
             avatar=avatar_path)
    try:
        db.session.add(y)
        db.session.add(u)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False


def get_user_by_id(user_id):
   return User.query.get(user_id)


def cart_stats(cart):
    total_quantity, total_amount = 0, 0
    if cart:
        for p in cart.values():
            total_quantity = total_quantity + p["quantity"]
            total_amount = total_amount + p["quantity"] * p["price"]

    return total_quantity, total_amount

def add_receipt(cart):
    if cart and current_user.is_authenticated:
        receipt = Receipt(user_id=current_user.id)
        db.session.add(receipt)

        for p in list(cart.values()):
            detail = ReceiptDetail(receipt=receipt,
                                   book_id=int(p["id"]),
                                   quantity=p["quantity"],
                                   price=p["price"])
            db.session.add(detail)

        try:
            db.session.commit()
            return True
        except Exception as ex:
            print(ex)

    return False