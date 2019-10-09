from flask import Blueprint, jsonify, request
from sqlAlchemy_db_instance import db
# from app import Todo

todos = [{"item": "Study SQL","id": 0, "done": "False"}]

todos_api = Blueprint('todos_api', __name__ )

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(500))
    done = db.Column(db.Boolean)

@todos_api.route('/todos', methods=['GET'])
def serve_all_todos():
    return jsonify({"items" : todos})

@todos_api.route('/todo', methods=['POST'])
def add_todo():
    todos.append({"item": request.json["item"],"id": 0, "done": "False"})
    todo = Todo()
    todo.item = request.json["item"]
    todo.done = False
    db.session.add(todo)
    db.session.commit()
    return jsonify(success=True)