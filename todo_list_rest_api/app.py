from flask import Flask, request

from services.todolists_service import TodosListService
from utils.generic_encoder import GenericEncoder

app = Flask(__name__)


service =TodosListService()
##endpoint pour récupérer la totalité des todosList => collection todoList
@app.route('/todolists', methods=['GET'])
def get_todolists():
    return GenericEncoder().encode(service.todos_lists)

###endpoint pour récupérer une seule todolist
@app.route('/todolists/<int:id>', methods=['GET'])
def get_todolist(id):
    try:
        t = service.get_todo_list(id)
        return GenericEncoder().encode(t)
    except:
        return "Not found", 404

##endpoint pour ajouter une todolist
@app.route('/todolists', methods=['POST'])
def post_todolist():
    title = request.json.get("title")
    todoslist = service.add_todo_list(title)
    return  GenericEncoder().encode(todoslist)

##endpoint pour supprimer la todolist
@app.route('/todolists/<int:id>', methods=['DELETE'])
def delete_todolist(id):
    if service.delete_todo_list(id):
        return "deleted todolist"
    return "Not found", 404


##endpoint pour mettre à jour la todolist
@app.route('/todolists/<int:id>', methods=['PUT'])
def update_todolist(id):
    return "update todolist"



##Ressource todoItems

##endpoint pour récupérer les todoitems d'une todolist
# @app.route('/todoitems/<int:todolist_id>', methods=['GET'])
# def get_todoitems(todolist_id):
#     return "list todoitems of todolist"

##version 2
@app.route('/todolists/<int:todolist_id>/todoitems', methods=['GET'])
def get_todoitems(todolist_id):
    return "list todoitems of todolist"

###Pour ajouter un todoitem dans une todolist
@app.route('/todolists/<int:todolist_id>/todoitems', methods=['POST'])
def post_todoitems(todolist_id):
    task_name = request.json.get("task_name")
    try:
        item = service.add_todoitem_to_todos_list(todolist_id, task_name)
        return GenericEncoder().encode(item)
    except:
        return "Not found", 404


###Pour supprimer un todoitem dans une todolist
@app.route('/todolists/<int:todolist_id>/todoitems/<int:todoitem_id>', methods=['DELETE'])
def delete_todoitems(todolist_id, todoitem_id):
    try:
        return service.delete_todoitem_from_todos_list(todolist_id, todoitem_id)

    except:
        return "Not found", 404

###Pour modifier un todoitem dans une todolist
@app.route('/todolists/<int:todolist_id>/todoitems/<int:todoitem_id>', methods=['PUT'])
def update_todoitems(todolist_id, todoitem_id):
    return "update todoitems of todolist"

if __name__ == '__main__':
    app.run()
