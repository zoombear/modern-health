from db import db


class SectionModel(db.Model):
    __tablename__ = 'sections'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    image_url = db.Column(db.String(80))
    order_index = db.Column(db.Integer)

    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    program = db.relationship('ProgramModel')

    activities = db.relationship('ActivityModel', lazy='dynamic')

    def __init__(self, name, description, image_url, order_index, program_id):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.order_index = order_index
        self.program_id = program_id

    def json(self):
        return {'name': self.name, 'description': self.description, 'image_url': self.image_url, 'order_index': self.order_index, 'activities': [activity.json() for activity in self.activities.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
