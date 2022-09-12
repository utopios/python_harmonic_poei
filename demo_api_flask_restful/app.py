from flask import Flask
from flask_restful import Api, Resource
from resources.demo_resource import DemoResource
app = Flask(__name__)

api = Api(app)



api.add_resource(DemoResource, '/', endpoint='first')
api.add_resource(DemoResource, '/demo', endpoint='second')

if __name__ == '__main__':
    app.run()
