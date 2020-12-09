import hashlib

from flask import render_template, request, url_for
from nha_sach import app, login, utils
from nha_sach.admin import *
from flask_login import login_user
import os

from nha_sach.models import User, UserRole


@app.route('/')
def index():
    typeofbooks = utils.read_data()
    return render_template('index.html', typeofbooks=typeofbooks)


@app.route('/book')
def book_list():
    tpbook_id = request.args.get('tpbook_id')
    kw = request.args.get('kw')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    books = utils.read_books(tpbook_id=tpbook_id, kw=kw, from_price=from_price, to_price=to_price)

    return render_template('book-list.html',
                           books=books)


@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = utils.get_book_by_id(book_id=book_id)
    return render_template('book-detail.html',
                           book=book)


@app.route('/login-user', methods=['POST', 'GET'])
def login_usr():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        user = User.query.filter(User.username == username.strip(),
                             User.password == password).first()
        if user:
            login_user(user=user)

    elif request.method == 'GET':
        return render_template('login_user.html')
<<<<<<< HEAD
    # url_for('index')
    return redirect('/')
=======

    return redirect(url_for('index'))
>>>>>>> 301e321a029854709cf2f8610020c4d530b3d4f2


@app.route('/login', methods=['POST', 'GET'])
def login_admin():
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

@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password == confirm:
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('username')
            gender = request.form.get('gender')
            avatar = request.files["avatar"]

            avatar_path = 'images/upload/%s' % avatar.filename
            avatar.save(os.path.join(app.root_path, 'static/', avatar_path))

<<<<<<< HEAD
            if utils.add_user(name=name, email=email, username=username, gender=gender,
=======
            if utils.add_user(name=name, email=email, username=username,
>>>>>>> 301e321a029854709cf2f8610020c4d530b3d4f2
                              password=password, avatar_path=avatar_path):
                return redirect('/')
            else:
                err_msg = "Hệ thống đang lỗi...Vui lòng đăng nhập lại sau!"
        else:
            err_msg = "Mật khẩu không khớp!"

    return render_template('registerUser.html', err_msg=err_msg)

@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)



if __name__ == '__main__':
    app.run(debug=True)
