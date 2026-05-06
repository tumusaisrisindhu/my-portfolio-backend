from flask import Blueprint, request, jsonify
from .service import get_all_todos, create_todo, delete_todo, update_todo

todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(get_all_todos())


@todo_bp.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    todo = create_todo(data)
    return jsonify(todo)


@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def remove_todo(todo_id):
    delete_todo(todo_id)
    return jsonify({"success": True})


@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"])
def edit_todo(todo_id):
    data = request.json
    updated = update_todo(todo_id, data)
    return jsonify(updated)