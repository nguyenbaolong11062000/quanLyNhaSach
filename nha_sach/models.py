from sqlalchemy import Column, Integer, String, Boolean, Enum, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from nha_sach import db
from flask_login import UserMixin
from enum import Enum as UserEnum
from datetime import datetime



class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class TypeOfBook(SaleBase):
    __tablename__ = 'typeofbook'

    books = relationship('Book',
                         backref='typeofbook', lazy=True)


class Book(SaleBase):
    __tablename__ = 'book'

    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    typeofbook_id = Column(Integer, ForeignKey(TypeOfBook.id),
                           nullable=False)
    receipt_detail = relationship('ReceiptDetail', backref='book', lazy=True)
    inventory_detail = relationship('InventoryDetailReport', backref='book', lazy=True)
    coupon_detail = relationship('CouponDetail', backref='book', lazy=True)
    bill_detail = relationship('BillDetail', backref='book', lazy=True)



class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100))
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    receipt = relationship('Receipt', backref='user', lazy=True)
    coupon_id = relationship('Coupon', backref='user', lazy=True)
    customer_id = relationship('Customer', backref='user', lazy=True)

    def __str__(self):
        return self.name

class Customer(SaleBase, UserMixin):
    __tablename__ = 'customer'
    identity_card = Column(String(20))
    email = Column(String(50))
    phone = Column(String(20))
    receipt = relationship('Receipt', backref='customer', lazy=True)
    bill = relationship('Bill', backref='customer', lazy=True)
    dept = relationship('DeptDetailReport', backref='customer', lazy=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)


class Receipt(db.Model):
    __tablename__ = 'receipt'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.today())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    customer_id = Column(Integer, ForeignKey(Customer.id), nullable=False)
    details = relationship('ReceiptDetail', backref="receipt", lazy=True)


class ReceiptDetail(db.Model):
    __tablename__ = 'receipt_detail'
    receipt_id = Column(Integer, ForeignKey(Receipt.id), primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id), nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)

class InventoryReport(db.Model):
    __tablename__ = 'inventory_report'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.today())
    inventory = relationship('InventoryDetailReport', backref='inventory_report', lazy=True)

class InventoryDetailReport(db.Model):
    __tablename__ = 'inventory_detail_report'
    inventory_id = Column(Integer, ForeignKey(InventoryReport.id), primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id),primary_key=True)
    quantity_before = Column(Integer, default=0)
    quantity_after = Column(Integer, default=0)
    arises = Column(String(100), nullable=False)

class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.today())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    coupon_detail = relationship('CouponDetail', backref='coupon', lazy=True)


class CouponDetail(db.Model):
    __tablename__ = 'coupon_detail'
    coupon_id = Column(Integer, ForeignKey(Coupon.id), primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id), primary_key=True)
    quantity = Column(Integer, default=0)

class Bill(db.Model):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.today())
    total = Column(Float, default=0)
    customer_id = Column(Integer, ForeignKey(Customer.id), nullable=False)
    bill_detail = relationship('BillDetail', backref='bill', lazy=True)

class BillDetail(db.Model):
    __tablename__ = 'bill_detail'
    bill_id = Column(Integer, ForeignKey(Bill.id), primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id), primary_key=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)

class DeptReport(db.Model):
    __tablename__ = 'dept_report'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.today())

class DeptDetailReport(db.Model):
    __tablename__ = 'dept_detail_report'

    dept_id = Column(Integer, ForeignKey(DeptReport.id), primary_key=True)
    customer_id = Column(Integer, ForeignKey(Customer.id), primary_key=True)
    money_before = Column(Float, default=0)
    money_after = Column(Float, default=0)
    arises = Column(String(100), nullable=False)

if __name__ == '__main__':
    db.create_all()