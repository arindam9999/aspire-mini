from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    repayments = db.relationship('Repayment')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    loans = db.relationship('Loan')


class Repayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'))