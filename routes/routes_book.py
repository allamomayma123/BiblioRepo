from flask import Blueprint, request, jsonify

from services.book_service import add_book, get_book_by_id, get_books, update_book, delete_book, sync_book_to_neo4j

from models.book import Book

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = Book.from_dict(data)
    add_book(book)
    sync_book_to_neo4j(book)
    return jsonify({"message": "Book added successfully"}), 201

@book_bp.route('/books/<book_id>', methods=['GET'])
def read_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({"message": "Book not found"}), 404

@book_bp.route('/books', methods=['GET'])
def read_all_books():
    books = get_books()
    return jsonify([book.to_dict() for book in books]), 200

@book_bp.route('/books/<book_id>', methods=['PUT'])
def update_book_route(book_id):
    data = request.get_json()
    update_book(book_id, data)
    return jsonify({"message": "Book updated successfully"}), 200

@book_bp.route('/books/<book_id>', methods=['DELETE'])
def delete_book_route(book_id):
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 200
