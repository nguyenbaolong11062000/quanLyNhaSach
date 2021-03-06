import hashlib

from flask import render_template, request, url_for, session, jsonify
from nha_sach import app, login, utils, decorator
from nha_sach.admin import *
from flask_login import login_user
import os, json

from nha_sach.models import Customer, User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/privacy-policy')
def pri_policy():
    return render_template('privacy-policy.html')


@app.route('/about-us')
def about_us():
   return render_template('about-us.html')


@app.route('/book')
@decorator.login_required
def book_list():
    tpbook_id = request.args.get('typeofbook_id')
    typebook = request.args.get('typebook')
    kw = request.args.get('kw')
    kw2 = request.args.get('kw2')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    books = utils.read_books(tpbook_id=tpbook_id, typebook=typebook, kw=kw, kw2=kw2, from_price=from_price, to_price=to_price)
    return render_template('book-list.html',
                           books=books, tpbook_id=tpbook_id)


@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = utils.get_book_by_id(book_id=book_id)
    return render_template('book-detail.html',
                           book=book)


@app.route('/login-user', methods=['POST', 'GET'])
def login_usr():
    err_msg = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = User.query.filter(User.username == username.strip(),
                             User.password == password).first()
        if user:
            login_user(user=user)
            if "next" in request.args:
                return redirect(request.args.get('next'))
            else:
                return redirect(url_for("index"))
        else:
            err_msg = "Login unsuccessful!"


    return render_template("login_user.html", err_msg=err_msg)


@app.route('/login', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')

        user = utils.check_login(username=username,
                                 password=password)
        if user:
            login_user(user=user)

    return redirect('/admin')

@app.route('/logout')
def logout_usr():
    logout_user()
    return redirect(url_for('index'))


@app.route('/registerCustomer', methods=['get', 'post'])
def registerCustomer():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password == confirm:
            phone = request.form.get('phone')
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('username')
            gender = request.form.get('gender')
            avatar = request.files["avatar"]

            avatar_path = 'images/upload/%s' % avatar.filename
            avatar.save(os.path.join(app.root_path, 'static/', avatar_path))

            if utils.add_user(name=name, email=email, phone=phone,
                              username=username, gender=gender,
                              password=password, avatar_path=avatar_path):
                return redirect('/')
            else:
                err_msg = "The system is faulty ... Please login again later!"
        else:
            err_msg = "Password incorrect!"

    return render_template('registerCustomer.html', err_msg=err_msg)



@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route('/api/cart', methods=['post'])
def cart():
    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']

    data = json.loads(request.data)
    id = str(data.get("id"))
    name = data.get("name")
    price = data.get("price")

    if id in cart:
        cart[id]["quantity"] = cart[id]["quantity"] + 1
    else:
        cart[id] = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        }

    session['cart'] = cart

    quan, price = utils.cart_stats(cart)

    return jsonify({
        "total_amount": price,
        "total_quantity": quan
    })

@app.route('/payment')
@decorator.login_required
def payment():
    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        "total_amount": price,
        "total_quantity": quan
    }
    return render_template('payment.html',
                           cart_info=cart_info)


@app.route('/api/pay', methods=['post'])
def pay():
    if utils.add_receipt(session.get('cart')):
        del session['cart']
        return jsonify({'message': 'Add receipt successful!'})

    return jsonify({'message': 'failed'})



@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)
if __name__ == '__main__':
    app.run(debug=True)
