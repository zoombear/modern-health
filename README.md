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
