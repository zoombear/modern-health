from flask_restful import Resource
from models.program import ProgramModel


class Program(Resource):
    def get(self, name):
        program = ProgramModel.find_by_name(name)
        if program:
            return program.json()
        return {'message': 'program not found'}, 404

    def post(self, name):
        if ProgramModel.find_by_name(name):
            return {'message': "A program with name '{}' already exists.".format(name)}, 400

        program = ProgramModel(name)
        try:
            program.save_to_db()
        except:
            return {"message": "An error occurred creating the program."}, 500

        return program.json(), 201

    def delete(self, name):
        program = ProgramModel.find_by_name(name)
        if program:
            program.delete_from_db()

        return {'message': 'program deleted'}


class ProgramList(Resource):
    def get(self):
        return {'programs': list(map(lambda x: x.json(), ProgramModel.query.all()))}
