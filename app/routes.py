from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from .. import get_db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()
    user = db.utilisateurs.find_one({"email": data['email']})
    if not user or not check_password_hash(user['mot_de_passe'], data['mot_de_passe']):
        return jsonify({'message': 'Identifiants invalides!'}), 401

    token = jwt.encode({
        'user_id': str(user['_id']),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, 'your_secret_key')
    return jsonify({'token': token})
