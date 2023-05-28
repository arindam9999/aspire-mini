from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql import func
from .models import Loan, Repayment
from . import db
import json
from datetime import datetime, timedelta

views = Blueprint('views', __name__)

@views.route('/repayment', methods=['GET', 'POST'])
@login_required
def repayment():
    if request.method == 'POST':
        repayment_id = int(request.form.get('repayment_id'))
        amount = float(request.form.get('amount'))
        repayment  = Repayment.query.filter_by(id=repayment_id).first()
        if not repayment:
            return "Error! Repayment id not found", 400
        if amount != repayment.amount:
            return f"Error! Amount is not equal to {repayment.amount}", 400
        else:
            repayment.status = True
            db.session.commit()
            return "Repayment done successfully!", 200
    else:
        loans = Loan.query.filter_by(user_id=current_user.id).all()
        repayment_data = []
        for loan in loans:
            repayments = Repayment.query.filter_by(loan_id = loan.id).order_by(Repayment.date.asc()).all()
            repayments_arr = [{'id': repayment.id, 'amount': repayment.amount, 'status': repayment.status, 'date': repayment.date} for repayment in repayments]
            repayment_data.append({'id': loan.id, 'amount': loan.amount, 'status': loan.status, 'date': loan.date, 'repayments': repayments_arr})
        return jsonify(repayment_data), 200


@views.route('/loan', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        amount = float(request.form.get('amount'))
        if amount <= 0:
            return "Error! Amount less that or equal to 0", 400
        else:
            new_loan = Loan(amount=amount, user_id=current_user.id) 
            db.session.add(new_loan)
            db.session.commit()
        return "Request for loan submitted!", 200
    else:
        if current_user.is_admin:
            loans = Loan.query.all()
        else:
            loans = Loan.query.filter_by(user_id=current_user.id).all()
        loan_data = [{'id': loan.id, 'amount': loan.amount, 'status': loan.status, 'date': loan.date} for loan in loans]
        return jsonify(loan_data), 200


@views.route('/approve-loan', methods=['POST'])
@login_required
def approve_load(): 
    loan_id = int(request.form.get('loan_id'))
    loan = Loan.query.get(loan_id)
    if loan:
        if current_user.is_admin == True:
            loan.status = True
            db.session.commit()
            for i in range(1, 4):
                repayment = Repayment(amount=loan.amount/3, loan_id=loan_id, date=datetime.now() + timedelta(weeks=i))
                db.session.add(repayment)
                db.session.commit()
        else:
            return "Error! User is not admin", 400

        return "Loan status updated to approved", 200
    else:
        "Error! Loan not found", 400


