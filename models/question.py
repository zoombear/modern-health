from db import db


class QuestionModel(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(880))
    is_active = db.Column(db.Boolean)

    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    activity = db.relationship('ActivityModel')

    choices = db.relationship('ChoiceModel', lazy='dynamic')

    def __init__(self, question_text, is_active, activity_id):
        self.question_text = question_text
        self.is_active = is_active
        self.activity_id = activity_id

    def json(self):
        return {'question_text': self.question_text, 'is_active': self.is_active, 'choices': [choice.json() for choice in self.choices.all()]}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(question_id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
