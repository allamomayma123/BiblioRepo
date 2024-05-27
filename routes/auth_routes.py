from flask import Blueprint, request, jsonify
from auth.auth_service import register_user, authenticate_user, get_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        try:
            register_user(username, password)
            return jsonify({"message": "User registered successfully"}), 201
        except ValueError as e:
            return jsonify({"message": str(e)}), 400
    return jsonify({"message": "Invalid data"}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if authenticate_user(username, password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/user/<username>', methods=['GET'])
def get_user_info(username):
    user = get_user(username)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404
