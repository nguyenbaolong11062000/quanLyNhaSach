from flask_login import logout_user, current_user
from flask import redirect
from nha_sach import admin, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from nha_sach.models import *


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')


class AboutUsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')

class BookView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class InventoryReportView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class InventoryDetailReportView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated



class ReceiptView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class ReceiptDetailView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class DeptReportView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class DeptDetailReportView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class CouponView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class CouponDetailView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class BillView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class BillDetailView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class CustomerView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(BaseView):
    @expose('/')
    def logout(self):
        logout_user()

        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated



admin.add_view(BookView(Book, db.session))
admin.add_view(CustomerView(Customer, db.session))
admin.add_view(InventoryReportView(InventoryReport, db.session))
admin.add_view(InventoryDetailReportView(InventoryDetailReport, db.session))
admin.add_view(CouponView(Coupon, db.session))
admin.add_view(CouponDetailView(CouponDetail, db.session))
admin.add_view(BillView(Bill, db.session))
admin.add_view(BillDetailView(BillDetail, db.session))
admin.add_view(DeptReportView(DeptReport, db.session))
admin.add_view(DeptDetailReportView(DeptDetailReport, db.session))
admin.add_view(ReceiptView(Receipt, db.session))
admin.add_view(ReceiptDetailView(ReceiptDetail, db.session))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(AboutUsView(name='About Us'))
admin.add_view(LogoutView(name='Logout'))
