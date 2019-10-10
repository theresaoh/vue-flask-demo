from flask import Blueprint, jsonify, request
from sqlAlchemy_db_instance import db
# from app import Todo

todos_api = Blueprint('todos_api', __name__ )

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(500))
    done = db.Column(db.Boolean)

@todos_api.route('/todos', methods=['GET'])
def serve_all_todos():
    todo_instances = db.session.query(Todo).all()
    todo_items = [{"id": todo.id, "item": todo.item, "done": todo.done} for todo in todo_instances]
    return jsonify({"items" : todo_items})

@todos_api.route('/todo', methods=['POST'])
def add_todo():
    new_todo = Todo()
    new_todo.item = request.json["item"]
    new_todo.done = False
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(success=True)