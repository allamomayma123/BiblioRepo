from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


# Configuration MongoDB
def get_mongo_client():
    client = MongoClient('mongodb://localhost:27017/')
    return client


# Enregistrement de l'utilisateur
def register_user(username, password):
    client = get_mongo_client()
    db = client.library
    users_collection = db.users

    if users_collection.find_one({"username": username}):
        raise ValueError("Username already exists")

    hashed_password = generate_password_hash(password)
    user = {
        "username": username,
        "password": hashed_password
    }
    users_collection.insert_one(user)


# Authentification de l'utilisateur
def authenticate_user(username, password):
    client = get_mongo_client()
    db = client.library
    users_collection = db.users

    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user['password'], password):
        return True
    return False


# Récupérer l'utilisateur
def get_user(username):
    client = get_mongo_client()
    db = client.library
    users_collection = db.users

    user = users_collection.find_one({"username": username})
    if user:
        return {
            "username": user['username']
        }
    return None
