from flask import Flask

app = Flask(__name__)


class TodosList:
    pass

class TodoItem:
    pass

##endpoint pour récupérer la totalité des todosList => collection todoList
@app.route('/todolists', methods=['GET'])
def get_todolists():
    return "list todolist"

###endpoint pour récupérer une seule todolist
@app.route('/todolists/<int:id>', methods=['GET'])
def get_todolist(id):
    return "todolist with id : "+id

##endpoint pour ajouter une todolist
@app.route('/todolists', methods=['POST'])
def post_todolist():
    return "add todolist"

##endpoint pour supprimer la todolist
@app.route('/todolists/<int:id>', methods=['DELETE'])
def delete_todolist(id):
    return "delete todolist"

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
    return "add todoitems of todolist"

###Pour supprimer un todoitem dans une todolist
@app.route('/todolists/<int:todolist_id>/todoitems/<int:todoitem_id>', methods=['DELETE'])
def delete_todoitems(todolist_id, todoitem_id):
    return "delete todoitems of todolist"

###Pour modifier un todoitem dans une todolist
@app.route('/todolists/<int:todolist_id>/todoitems/<int:todoitem_id>', methods=['PUT'])
def update_todoitems(todolist_id, todoitem_id):
    return "update todoitems of todolist"

if __name__ == '__main__':
    app.run()
