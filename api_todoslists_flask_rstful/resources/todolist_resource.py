from flask_restful import Resource, reqparse
from flask import request
from services.todos_service import TodosService
from utils.generic_encoder import GenericEncoder


class TodoListResource(Resource):

    ##Un objet qui permet de lire les données envoyées dans la requetes (json form,...)
    parser = reqparse.RequestParser()
    ##Configuration des paramètres à récupérer
    parser.add_argument('title', type=str, required=True, help="Title obligatoire")
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

        ###On récupère les données à partir de l'objet request
        #title = request.json.get("title")
        ## on peut également utiliser les reqparse de flask-restful pour récupérer les params.
        #on utilise le parser, avec la méthode parse_args
        data = TodoListResource.parser.parse_args()
        todoslist = self.service.add_todo_list(data["title"])
        return GenericEncoder().encode(todoslist)

    def delete(self):
        pass

