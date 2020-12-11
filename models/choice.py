from db import db


class ChoiceModel(db.Model):
    __tablename__ = 'choices'
    choice_id = db.Column(db.Integer, primary_key=True)
    choice_text = db.Column(db.String(880))
    is_correct = db.Column(db.Boolean)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    question = db.relationship('QuestionModel')

    def __init__(self, choice_text, is_correct):
        self.choice_text = choice_text
        self.is_correct = is_correct

    def json(self):
        return {'choice_text': self.choice_text, 'is_correct': self.is_correct}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(choice_id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
