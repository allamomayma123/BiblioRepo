from flask import Blueprint, request, jsonify
from models.loan import Loan
from services.loan_service import add_loan, get_loan, get_all_loans, update_loan, delete_loan

loan_bp = Blueprint('loan', __name__)

@loan_bp.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()
    loan = Loan.from_dict(data)
    add_loan(loan)
    return jsonify({"message": "Loan added successfully"}), 201

@loan_bp.route('/loans/<loan_id>', methods=['GET'])
def read_loan(loan_id):
    loan = get_loan(loan_id)
    if loan:
        return jsonify(loan.to_dict()), 200
    return jsonify({"message": "Loan not found"}), 404

@loan_bp.route('/loans', methods=['GET'])
def read_all_loans():
    loans = get_all_loans()
    return jsonify([loan.to_dict() for loan in loans]), 200

@loan_bp.route('/loans/<loan_id>', methods=['PUT'])
def update_loan_route(loan_id):
    data = request.get_json()
    update_loan(loan_id, data)
    return jsonify({"message": "Loan updated successfully"}), 200

@loan_bp.route('/loans/<loan_id>', methods=['DELETE'])
def delete_loan_route(loan_id):
    delete_loan(loan_id)
    return jsonify({"message": "Loan deleted successfully"}), 200
