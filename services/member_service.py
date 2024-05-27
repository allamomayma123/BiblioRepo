from config.mongo_config import get_mongo_client
from models.member import Member


# MongoDB Operations
def add_member(member: Member):
    client = get_mongo_client()
    db = client.library
    members_collection = db.members
    members_collection.insert_one(member.to_dict())

def get_member(member_id):
    client = get_mongo_client()
    db = client.library
    members_collection = db.members
    member_data = members_collection.find_one({"_id": member_id})
    if member_data:
        return Member.from_dict(member_data)
    return None

def get_all_members():
    client = get_mongo_client()
    db = client.library
    members_collection = db.members
    members = members_collection.find()
    return [Member.from_dict(member) for member in members]

def update_member(member_id, data):
    client = get_mongo_client()
    db = client.library
    members_collection = db.members
    members_collection.update_one({"_id": member_id}, {"$set": data})

def delete_member(member_id):
    client = get_mongo_client()
    db = client.library
    members_collection = db.members
    members_collection.delete_one({"_id": member_id})
