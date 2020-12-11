from flask_restful import Resource
from models.choice import ChoiceModel


class Choice(Resource):
    def get(self, id):
        choice = ChoiceModel.find_by_id(id)
        if choice:
            return choice.json()
        return {'message': 'choice not found'}, 404

    def post(self, id):
        if ChoiceModel.find_by_id(id):
            return {'message': "A choice with id '{}' already exists.".format(id)}, 400

        choice = ChoiceModel(id)
        try:
            choice.save_to_db()
        except:
            return {"message": "An error occurred creating the choice."}, 500

        return choice.json(), 201

    def delete(self, id):
        choice = ChoiceModel.find_by_id(id)
        if choice:
            choice.delete_from_db()

        return {'message': 'choice deleted'}


class ChoiceList(Resource):
    def get(self):
        return {'choices': list(map(lambda x: x.json(), ChoiceModel.query.all()))}
