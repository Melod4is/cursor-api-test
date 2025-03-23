from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
from app.schemas.user import user_schema

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify(users)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify(user), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data)
    return jsonify(user)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return '', 204 