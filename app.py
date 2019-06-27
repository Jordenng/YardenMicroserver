from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

users = [
    {
        "name": "yarden",
        "age": 23,
        "occupation": "Engineer"
    },
    {
        "name": "Artur",
        "age": 30,
        "occupation": "Engineer"

    },
    {
        "name": "Tapak",
        "age": 3,
        "occupation": "Cat"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                return "User with the name {} already exist".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200



api.add_resource(User, "/user/<string:name>")

if __name__ == '__main__':
    app.run()
