from config.mongo_config import get_mongo_client
from models.loan import Loan


# MongoDB Operations
def add_loan(loan: Loan):
    client = get_mongo_client()
    db = client.library
    loans_collection = db.loans
    loans_collection.insert_one(loan.to_dict())

def get_loan(loan_id):
    client = get_mongo_client()
    db = client.library
    loans_collection = db.loans
    loan_data = loans_collection.find_one({"_id": loan_id})
    if loan_data:
        return Loan.from_dict(loan_data)
    return None

def get_all_loans():
    client = get_mongo_client()
    db = client.library
    loans_collection = db.loans
    loans = loans_collection.find()
    return [Loan.from_dict(loan) for loan in loans]

def update_loan(loan_id, data):
    client = get_mongo_client()
    db = client.library
    loans_collection = db.loans
    loans_collection.update_one({"_id": loan_id}, {"$set": data})

def delete_loan(loan_id):
    client = get_mongo_client()
    db = client.library
    loans_collection = db.loans
    loans_collection.delete_one({"_id": loan_id})
