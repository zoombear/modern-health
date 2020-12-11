# Third party modules
import pytest

# First party modules
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_program(client):
    rv = client.get("/program/Cognitive Behavioral Therapy")
    expected_data = b'{"name": "Cognitive Behavioral Therapy", "description": "Cognitive Behavioral Therapy description", "sections": [{"name": "Section 11", "description": "Section 11 description", "image_url": "https://placekitten.com/200/200", "order_index": 11, "activities": []}, {"name": "Section 12", "description": "Section 12 description", "image_url": "https://placekitten.com/200/200", "order_index": 12, "activities": []}, {"name": "Section 13", "description": "Section 13 description", "image_url": "https://placekitten.com/200/200", "order_index": 13, "activities": []}, {"name": "Section 14", "description": "Section 14 description", "image_url": "https://placekitten.com/200/200", "order_index": 14, "activities": []}, {"name": "Section 15", "description": "Section 15 description", "image_url": "https://placekitten.com/200/200", "order_index": 15, "activities": []}, {"name": "Section 16", "description": "Section 16 description", "image_url": "https://placekitten.com/200/200", "order_index": 16, "activities": []}, {"name": "Section 17", "description": "Section 17 description", "image_url": "https://placekitten.com/200/200", "order_index": 17, "activities": []}, {"name": "Section 18", "description": "Section 18 description", "image_url": "https://placekitten.com/200/200", "order_index": 18, "activities": []}]}\n'
    assert expected_data == rv.data


def test_program_invalid(client):
    rv = client.get("/program/Nonexisted program")
    expected_data = b'{"message": "program not found"}\n'
    expected_status = 404
    assert expected_data == rv.data
    assert expected_status == rv.status_code


def test_programs(client):
    rv = client.get("/programs")
    expected_data = b'{"programs": [{"name": "Leadership Development Program", "description": "Leadership Development Program description", "sections": [{"name": "Section 1", "description": "Section 1 description", "image_url": "https://placekitten.com/200/200", "order_index": 1, "activities": [{"raw_html": "<div>Hello world</div>", "questions": [{"question_text": "First question text", "is_active": true, "choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}]}]}, {"name": "Section 2", "description": "Section 2 description", "image_url": "https://placekitten.com/200/200", "order_index": 2, "activities": []}, {"name": "Section 3", "description": "Section 3 description", "image_url": "https://placekitten.com/200/200", "order_index": 3, "activities": []}, {"name": "Section 4", "description": "Section 4 description", "image_url": "https://placekitten.com/200/200", "order_index": 4, "activities": []}, {"name": "Section 5", "description": "Section 5 description", "image_url": "https://placekitten.com/200/200", "order_index": 5, "activities": []}, {"name": "Section 6", "description": "Section 6 description", "image_url": "https://placekitten.com/200/200", "order_index": 6, "activities": []}, {"name": "Section 7", "description": "Section 7 description", "image_url": "https://placekitten.com/200/200", "order_index": 7, "activities": []}, {"name": "Section 8", "description": "Section 8 description", "image_url": "https://placekitten.com/200/200", "order_index": 8, "activities": []}, {"name": "Section 9", "description": "Section 9 description", "image_url": "https://placekitten.com/200/200", "order_index": 9, "activities": []}, {"name": "Section 10", "description": "Section 10 description", "image_url": "https://placekitten.com/200/200", "order_index": 10, "activities": []}]}, {"name": "Cognitive Behavioral Therapy", "description": "Cognitive Behavioral Therapy description", "sections": [{"name": "Section 11", "description": "Section 11 description", "image_url": "https://placekitten.com/200/200", "order_index": 11, "activities": []}, {"name": "Section 12", "description": "Section 12 description", "image_url": "https://placekitten.com/200/200", "order_index": 12, "activities": []}, {"name": "Section 13", "description": "Section 13 description", "image_url": "https://placekitten.com/200/200", "order_index": 13, "activities": []}, {"name": "Section 14", "description": "Section 14 description", "image_url": "https://placekitten.com/200/200", "order_index": 14, "activities": []}, {"name": "Section 15", "description": "Section 15 description", "image_url": "https://placekitten.com/200/200", "order_index": 15, "activities": []}, {"name": "Section 16", "description": "Section 16 description", "image_url": "https://placekitten.com/200/200", "order_index": 16, "activities": []}, {"name": "Section 17", "description": "Section 17 description", "image_url": "https://placekitten.com/200/200", "order_index": 17, "activities": []}, {"name": "Section 18", "description": "Section 18 description", "image_url": "https://placekitten.com/200/200", "order_index": 18, "activities": []}]}, {"name": "New Parenting", "description": "New Parenting description", "sections": [{"name": "Section 19", "description": "Section 19 description", "image_url": "https://placekitten.com/200/200", "order_index": 19, "activities": []}, {"name": "Section 20", "description": "Section 20 description", "image_url": "https://placekitten.com/200/200", "order_index": 20, "activities": []}, {"name": "Section 21", "description": "Section 21 description", "image_url": "https://placekitten.com/200/200", "order_index": 21, "activities": []}, {"name": "Section 22", "description": "Section 22 description", "image_url": "https://placekitten.com/200/200", "order_index": 22, "activities": []}]}, {"name": "Mindful Communication Program", "description": "Mindful Communication description", "sections": [{"name": "Section 23", "description": "Section 23 description", "image_url": "https://placekitten.com/200/200", "order_index": 23, "activities": []}, {"name": "Section 24", "description": "Section 24 description", "image_url": "https://placekitten.com/200/200", "order_index": 24, "activities": []}, {"name": "Section 25", "description": "Section 25 description", "image_url": "https://placekitten.com/200/200", "order_index": 25, "activities": []}, {"name": "Section 26", "description": "Section 26 description", "image_url": "https://placekitten.com/200/200", "order_index": 26, "activities": []}]}]}\n'
    assert expected_data == rv.data


def test_section(client):
    rv = client.get("/section/Section 3")
    expected_data = b'{"name": "Section 3", "description": "Section 3 description", "image_url": "https://placekitten.com/200/200", "order_index": 3, "activities": []}\n'
    assert expected_data == rv.data


def test_sections(client):
    rv = client.get("/sections")
    expected_data = b'{"sections": [{"name": "Section 1", "description": "Section 1 description", "image_url": "https://placekitten.com/200/200", "order_index": 1, "activities": [{"raw_html": "<div>Hello world</div>", "questions": [{"question_text": "First question text", "is_active": true, "choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}]}]}, {"name": "Section 2", "description": "Section 2 description", "image_url": "https://placekitten.com/200/200", "order_index": 2, "activities": []}, {"name": "Section 3", "description": "Section 3 description", "image_url": "https://placekitten.com/200/200", "order_index": 3, "activities": []}, {"name": "Section 4", "description": "Section 4 description", "image_url": "https://placekitten.com/200/200", "order_index": 4, "activities": []}, {"name": "Section 5", "description": "Section 5 description", "image_url": "https://placekitten.com/200/200", "order_index": 5, "activities": []}, {"name": "Section 6", "description": "Section 6 description", "image_url": "https://placekitten.com/200/200", "order_index": 6, "activities": []}, {"name": "Section 7", "description": "Section 7 description", "image_url": "https://placekitten.com/200/200", "order_index": 7, "activities": []}, {"name": "Section 8", "description": "Section 8 description", "image_url": "https://placekitten.com/200/200", "order_index": 8, "activities": []}, {"name": "Section 9", "description": "Section 9 description", "image_url": "https://placekitten.com/200/200", "order_index": 9, "activities": []}, {"name": "Section 10", "description": "Section 10 description", "image_url": "https://placekitten.com/200/200", "order_index": 10, "activities": []}, {"name": "Section 11", "description": "Section 11 description", "image_url": "https://placekitten.com/200/200", "order_index": 11, "activities": []}, {"name": "Section 12", "description": "Section 12 description", "image_url": "https://placekitten.com/200/200", "order_index": 12, "activities": []}, {"name": "Section 13", "description": "Section 13 description", "image_url": "https://placekitten.com/200/200", "order_index": 13, "activities": []}, {"name": "Section 14", "description": "Section 14 description", "image_url": "https://placekitten.com/200/200", "order_index": 14, "activities": []}, {"name": "Section 15", "description": "Section 15 description", "image_url": "https://placekitten.com/200/200", "order_index": 15, "activities": []}, {"name": "Section 16", "description": "Section 16 description", "image_url": "https://placekitten.com/200/200", "order_index": 16, "activities": []}, {"name": "Section 17", "description": "Section 17 description", "image_url": "https://placekitten.com/200/200", "order_index": 17, "activities": []}, {"name": "Section 18", "description": "Section 18 description", "image_url": "https://placekitten.com/200/200", "order_index": 18, "activities": []}, {"name": "Section 19", "description": "Section 19 description", "image_url": "https://placekitten.com/200/200", "order_index": 19, "activities": []}, {"name": "Section 20", "description": "Section 20 description", "image_url": "https://placekitten.com/200/200", "order_index": 20, "activities": []}, {"name": "Section 21", "description": "Section 21 description", "image_url": "https://placekitten.com/200/200", "order_index": 21, "activities": []}, {"name": "Section 22", "description": "Section 22 description", "image_url": "https://placekitten.com/200/200", "order_index": 22, "activities": []}, {"name": "Section 23", "description": "Section 23 description", "image_url": "https://placekitten.com/200/200", "order_index": 23, "activities": []}, {"name": "Section 24", "description": "Section 24 description", "image_url": "https://placekitten.com/200/200", "order_index": 24, "activities": []}, {"name": "Section 25", "description": "Section 25 description", "image_url": "https://placekitten.com/200/200", "order_index": 25, "activities": []}, {"name": "Section 26", "description": "Section 26 description", "image_url": "https://placekitten.com/200/200", "order_index": 26, "activities": []}]}\n'
    assert expected_data == rv.data


def test_activity(client):
    rv = client.get("/activity/1")
    expected_data = b'{"raw_html": "<div>Hello world</div>", "questions": [{"question_text": "First question text", "is_active": true, "choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}]}\n'
    assert expected_data == rv.data


def test_activities(client):
    rv = client.get("/activities")
    expected_data = b'{"activities": [{"raw_html": "<div>Hello world</div>", "questions": [{"question_text": "First question text", "is_active": true, "choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}]}]}\n'
    assert expected_data == rv.data


def test_question(client):
    rv = client.get("/question/1")
    expected_data = b'{"question_text": "First question text", "is_active": true, "choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}\n'
    assert expected_data == rv.data


def test_questions(client):
    rv = client.get("/questions")
    expected_data = b'{"questions": [{"question_text": "First question text", "is_active": true, "choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}]}\n'
    assert expected_data == rv.data


def test_choice(client):
    rv = client.get("/choice/1")
    expected_data = b'{"choice_text": "first choice text", "is_correct": true}\n'
    assert expected_data == rv.data


def test_choices(client):
    rv = client.get("/choices")
    expected_data = b'{"choices": [{"choice_text": "first choice text", "is_correct": true}, {"choice_text": "second choice text", "is_correct": false}, {"choice_text": "third choice text", "is_correct": false}, {"choice_text": "fourth choice text", "is_correct": false}]}\n'
    assert expected_data == rv.data
