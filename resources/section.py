from flask_restful import Resource
from models.section import SectionModel


class Section(Resource):
    def get(self, name):
        section = SectionModel.find_by_name(name)
        if section:
            return section.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if SectionModel.find_by_name(name):
            return {'message': "A section with name '{}' already exists.".format(name)}, 400

        section = SectionModel(name)
        try:
            section.save_to_db()
        except:
            return {"message": "An error occurred creating the section."}, 500

        return section.json(), 201

    def delete(self, name):
        section = SectionModel.find_by_name(name)
        if section:
            section.delete_from_db()

        return {'message': 'Section deleted'}


class SectionList(Resource):
    def get(self):
        return {'sections': list(map(lambda x: x.json(), SectionModel.query.all()))}
