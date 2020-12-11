from db import db


class ActivityModel(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    raw_html = db.Column(db.String(880))
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))
    section = db.relationship('SectionModel')
    questions = db.relationship('QuestionModel', lazy='dynamic')

    def __init__(self, raw_html, section_id):
        self.raw_html = raw_html
        self.section_id = section_id

    def json(self):
        return {'raw_html': self.raw_html, 'questions': [question.json() for question in self.questions.all()]}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
