from flask import Blueprint, request, jsonify
from models.author import Author
from services.author_service import add_author, get_author_by_id, get_authors, update_author, delete_author

author_bp = Blueprint('author', __name__)

@author_bp.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    author = Author.from_dict(data)
    add_author(author)
    return jsonify({"message": "Author added successfully"}), 201

@author_bp.route('/authors/<name>', methods=['GET'])
def read_author(name):
    author = get_author_by_id(name)
    if author:
        return jsonify(author.to_dict()), 200
    return jsonify({"message": "Author not found"}), 404

@author_bp.route('/authors', methods=['GET'])
def read_all_authors():
    authors = get_authors()
    return jsonify([author.to_dict() for author in authors]), 200

@author_bp.route('/authors/<name>', methods=['PUT'])
def update_author_route(name):
    data = request.get_json()
    update_author(name, data)
    return jsonify({"message": "Author updated successfully"}), 200

@author_bp.route('/authors/<name>', methods=['DELETE'])
def delete_author_route(name):
    delete_author(name)
    return jsonify({"message": "Author deleted successfully"}), 200
