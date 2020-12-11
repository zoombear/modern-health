from flask_restful import Resource
from models.question import QuestionModel


class Question(Resource):
    def get(self, id):
        question = QuestionModel.find_by_id(id)
        if question:
            return question.json()
        return {'message': 'Question not found'}, 404

    def post(self, id):
        if QuestionModel.find_by_id(id):
            return {'message': "A question with id '{}' already exists.".format(id)}, 400

        question = QuestionModel(id)
        try:
            question.save_to_db()
        except:
            return {"message": "An error occurred creating the question."}, 500

        return question.json(), 201

    def delete(self, id):
        question = QuestionModel.find_by_id(id)
        if question:
            question.delete_from_db()

        return {'message': 'question deleted'}


class QuestionList(Resource):
    def get(self):
        return {'questions': list(map(lambda x: x.json(), QuestionModel.query.all()))}
