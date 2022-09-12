from flask import Flask
from flask_restful import Api

from resources.todolist_resource import TodoListResource
from resources.todoitem_resource import TodoitemResource
app = Flask(__name__)

api = Api(app)

##Ajoute les ressources

# api.add_resource(TodoListResource, '/todolist', endpoint='todolist')
# api.add_resource(TodoListResource, '/todolist/<int:id>', endpoint='todolist_id')

# En une seule fois
#resource todolist
api.add_resource(TodoListResource, '/todolist', '/todolist/<int:id>', endpoint='todolist')

#resource todoitem
api.add_resource(TodoitemResource, '/todolist/<int:todolist_id>/todoitems', '/todolist/<int:todolist_id>/todoitems/<int:id>', endpoint='todoitems')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
