from flask import Flask

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
@app.route('/', methods=['GET'])
def get_persons():
    return persons

##Route pour ajouter une personne
@app.route('/', methods=['POST'])
def add_person():
    return 'action for add person'

##Route pour modifier une personne
@app.route('/', methods=['PUT'])
def update_person():
    return 'action for update person'

##Route pour delete une personne
@app.route('/', methods=['DELETE'])
def delete_person():
    return 'action for delete person'

if __name__ == '__main__':
    app.run(debug=True)
