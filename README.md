## Setup

1 - Create your virtual environment.

```
pip3 install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
```

2 - Install requirements:

```
pip install -r requirements.txt
```

3 - Run the server:

```
python app.py
```

## Seed Data

While your virtual env is running, run this script to seed db:

```
python create_tables.py
```

## Testing

While your virtual env is running, run this command to run tests:

```
pytest
```

## General Thoughts

In order to stand up a Python micro service my go-to is usually Flask since I find it very straightforward for API development. So for this assignment I generated a simple [Flask](https://flask.palletsprojects.com/en/1.1.x/) app.

I broke down the data requirements and developed a data model that would make sense for the needs of a client querying data en masse to be saved in Redux or possibly record by record depending on the user/view called from the frontend to the API. I created tables and models for each segment of the data. I may have overdone things a bit by writing up the logic to add and delete records through the API. I did not add tests for that logic since it isn’t required for the specifications of the assignment. I decided to leave the code in anyways, I hope that’s ok!

For the database, I choice [Sqlite](https://www.sqlite.org/index.html) instead of [Postgres](https://www.postgresql.org/). I figured a relational database was all that was asked for and Sqlite is super straightforward to set up quickly, so I went with that solution. For testing I used simple [Pytest](https://flask.palletsprojects.com/en/1.1.x/testing/) for some unit testing of the API endpoints.

I debated adding a user model, authentication, and a table to save the user’s answers. Since those weren’t asked for in the spec, I left those ideas out.
