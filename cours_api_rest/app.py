from flask import Flask, request

app = Flask(__name__)

#app.config["FLASK_DEBUG"] = True

persons = ["toto", "tata", "titi"]

# @app.route('/toto')
# def handle_toto():
#     return 'Hello from toto'
#
# @app.route('/tata')
# def handle_tata():
#     return 'Hello from tata'
#
# @app.route('/titi')
# def handle_titi():
#     return 'Hello from tata'
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

###L'ajout d'une route http à gérer par flask avec les verbs GET, POST
##Route pour Récupérer les personnes
# @app.route('/', methods=['GET'])
# def get_persons():
#     return persons
#
# ##Route pour ajouter une personne
# @app.route('/', methods=['POST'])
# def add_person():
#     return 'action for add person'
#
# ##Route pour modifier une personne
# @app.route('/', methods=['PUT'])
# def update_person():
#     return 'action for update person'
#
# ##Route pour delete une personne
# @app.route('/', methods=['DELETE'])
# def delete_person():
#     return 'action for delete person'


##Routes avec un niveau 1
# @app.route('/getPersons', methods=['POST'])
# def get_persons():
#     return persons
#
# ###Pour récupérer les paramètres d'une requête
# ###Flask met à disposition un objet request
# @app.route('/getPerson', methods=['POST'])
# def get_person():
#     return persons[request.args.id]
#
# @app.route('/addPerson', methods=['POST'])
# def add_persons():
#     return 'add person'
#
# @app.route('/updatePerson', methods=['POST'])
# def update_persons():
#     return 'update person'

##routes avec niveau 2
##Personnes
@app.route('/persons', methods=['GET'])
def get_persons():
    return persons

@app.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    return persons[id]



@app.route('/persons', methods=['POST'])
def post_person():
    return 'post'

@app.route('/persons', methods=['PUT'])
def put_person():
    return 'put'

@app.route('/persons', methods=['DELETE'])
def delete_person():
    return 'delete'

# ##Adresses
# @app.route('/addresses', methods=['GET'])
# def get_addresses():
#     return persons
#
# @app.route('/addresses', methods=['POST'])
# def post_addresses():
#     return 'post'
#
# @app.route('/addresses', methods=['PUT'])
# def put_addresses():
#     return 'put'
#
# @app.route('/addresses', methods=['DELETE'])
# def delete_addresses():
#     return 'delete'


if __name__ == '__main__':
    app.run(debug=True)
