from flask import Flask
from flask_restful import Api

from resources.todolist_resource import TodoListResource

app = Flask(__name__)

api = Api(app)

##Ajoute les ressources

# api.add_resource(TodoListResource, '/todolist', endpoint='todolist')
# api.add_resource(TodoListResource, '/todolist/<int:id>', endpoint='todolist_id')

# En une seule fois
api.add_resource(TodoListResource, '/todolist', '/todolist/<int:id>', endpoint='todolist')


if __name__ == '__main__':
    app.run()
