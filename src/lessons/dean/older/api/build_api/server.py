# pip install flask
# pip install flask-restful

from flask import Flask
from flask_restful import Resource, Api


class Employees(Resource):
    def get(self):
        return "hello Dean"


class Tracks(Resource):
    def get(self):
        return "wheels on bus"


def main():
    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Employees, "/employees")  # Route_1
    api.add_resource(Tracks, "/tracks")  # Route=_2

    app.run(port="5000")


if __name__ == "__main__":
    main()
