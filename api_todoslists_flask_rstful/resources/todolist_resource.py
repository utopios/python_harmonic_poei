from flask_restful import Resource
from flask import request
from services.todos_service import TodosService
from utils.generic_encoder import GenericEncoder


class TodoListResource(Resource):
    def __init__(self):
        self.service = TodosService()

    #Les args d'url sont récupérés directement comme paramètre dans la méthode
    def get(self, id = None):
        if id is None:
            return self.service.todos_lists
        else:
            try:
                return self.service.get_todo_list(id)
            except ValueError as err:
                return str(err), 404

    def post(self):
        title = request.json.get("title")
        todoslist = self.service.add_todo_list(title)
        return GenericEncoder().encode(todoslist)

    def delete(self):
        pass

