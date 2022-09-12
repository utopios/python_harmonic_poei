from flask_restful import Resource

class DemoResource(Resource):
    def get(self):
        return {"message": "demo api"}

    def post(self):
        return {"message":  "post ressource"}

    def put(self):
        return {"message": "put"}

    def delete(self):
        return {"message": "delete"}