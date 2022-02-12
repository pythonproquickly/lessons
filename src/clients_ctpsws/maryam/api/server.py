from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify


class Employees(Resource):
    def get(self):
        # lots can happen here...

        # and here is where the results are returned
        return jsonify({"message": "hello from Employees"})


class Tracks(Resource):
    def get(self):
        return jsonify({"message": "hello from Tracks"})


class EmployeesName(Resource):
    def get(self, employee_id: int):
        return jsonify({"message": f"hello from EmployeesName {employee_id}"})


def main():

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Employees, "/employees")
    api.add_resource(Tracks, "/tracks")
    api.add_resource(EmployeesName, "/employees/<employee_id>")

    app.run(port="5002")


if __name__ == "__main__":
    main()
