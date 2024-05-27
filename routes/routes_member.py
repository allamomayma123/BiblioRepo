from flask import Blueprint, request, jsonify
from models.member import Member
from services.member_service import add_member, get_member, get_all_members, update_member, delete_member

member_bp = Blueprint('member', __name__)

@member_bp.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    member = Member.from_dict(data)
    add_member(member)
    return jsonify({"message": "Member added successfully"}), 201

@member_bp.route('/members/<member_id>', methods=['GET'])
def read_member(member_id):
    member = get_member(member_id)
    if member:
        return jsonify(member.to_dict()), 200
    return jsonify({"message": "Member not found"}), 404

@member_bp.route('/members', methods=['GET'])
def read_all_members():
    members = get_all_members()
    return jsonify([member.to_dict() for member in members]), 200

@member_bp.route('/members/<member_id>', methods=['PUT'])
def update_member_route(member_id):
    data = request.get_json()
    update_member(member_id, data)
    return jsonify({"message": "Member updated successfully"}), 200

@member_bp.route('/members/<member_id>', methods=['DELETE'])
def delete_member_route(member_id):
    delete_member(member_id)
    return jsonify({"message": "Member deleted successfully"}), 200
