from db import db


class ProgramModel(db.Model):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))

    sections = db.relationship('SectionModel', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def json(self):
        return {'name': self.name, 'description': self.description, 'sections': [section.json() for section in self.sections.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
