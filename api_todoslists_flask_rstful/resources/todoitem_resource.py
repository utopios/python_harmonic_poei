from flask_restful import Resource
from flask import request
from services.todos_service import TodosService
from utils.generic_encoder import GenericEncoder


class TodoitemResource(Resource):

    def __init__(self):
        self.service = TodosService()

    def get(self, todolist_id, id):
        pass

    def post(self, todolist_id):

        task_name = request.json.get("task_name")
        try:
            item = self.service.add_todoitem_to_todos_list(todolist_id, task_name)
            return GenericEncoder().encode(item)
        except:
            return "Not found", 404
