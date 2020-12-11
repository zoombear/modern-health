from flask_restful import Resource
from models.activity import ActivityModel


class Activity(Resource):
    def get(self, id):
        activity = ActivityModel.find_by_id(id)
        if activity:
            return activity.json()
        return {'message': 'activity not found'}, 404

    def post(self, id):
        if ActivityModel.find_by_id(id):
            return {'message': "A activity with id '{}' already exists.".format(id)}, 400

        activity = ActivityModel(id)
        try:
            activity.save_to_db()
        except:
            return {"message": "An error occurred creating the activity."}, 500

        return activity.json(), 201

    def delete(self, id):
        activity = ActivityModel.find_by_id(id)
        if activity:
            activity.delete_from_db()

        return {'message': 'activity deleted'}


class ActivityList(Resource):
    def get(self):
        return {'activities': list(map(lambda x: x.json(), ActivityModel.query.all()))}
