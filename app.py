from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


from resources.activity import Activity, ActivityList
from resources.program import Program, ProgramList
from resources.section import Section, SectionList
from resources.question import Question, QuestionList
from resources.choice import Choice, ChoiceList

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = 'meow'
    api = Api(app)
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.add_resource(Activity, '/activity/<string:id>')
    api.add_resource(ActivityList, '/activities')
    api.add_resource(Program, '/program/<string:name>')
    api.add_resource(ProgramList, '/programs')
    api.add_resource(Section, '/section/<string:name>')
    api.add_resource(SectionList, '/sections')
    api.add_resource(Question, '/question/<string:id>')
    api.add_resource(QuestionList, '/questions')
    api.add_resource(Choice, '/choice/<string:id>')
    api.add_resource(ChoiceList, '/choices')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
