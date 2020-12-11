import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# PROGRAM

cursor.execute('''DROP TABLE IF EXISTS programs''')

cursor.execute('''CREATE TABLE IF NOT EXISTS programs
             (id INTEGER PRIMARY KEY, name text, description text)''')

records = [(1, 'Leadership Development Program', 'Leadership Development Program description'),
           (2, 'Cognitive Behavioral Therapy',
            'Cognitive Behavioral Therapy description'),
           (3, 'New Parenting', 'New Parenting description'),
           (4, 'Mindful Communication Program', 'Mindful Communication description')]

cursor.executemany(
    'INSERT INTO programs VALUES(?,?,?);', records)


# SECTION

cursor.execute('''DROP TABLE IF EXISTS sections''')

cursor.execute('''CREATE TABLE IF NOT EXISTS sections
             (id INTEGER PRIMARY KEY, name text, description text, image_url text, program_id integer, order_index integer)''')

records = [(1, 'Section 1', 'Section 1 description', 'https://placekitten.com/200/200', 1, 1),
           (2, 'Section 2', 'Section 2 description',
            'https://placekitten.com/200/200', 1, 2),
           (3, 'Section 3', 'Section 3 description',
            'https://placekitten.com/200/200', 1, 3),
           (4, 'Section 4', 'Section 4 description',
            'https://placekitten.com/200/200', 1, 4),
           (5, 'Section 5', 'Section 5 description',
            'https://placekitten.com/200/200', 1, 5),
           (6, 'Section 6', 'Section 6 description',
            'https://placekitten.com/200/200', 1, 6),
           (7, 'Section 7', 'Section 7 description',
            'https://placekitten.com/200/200', 1, 7),
           (8, 'Section 8', 'Section 8 description',
            'https://placekitten.com/200/200', 1, 8),
           (9, 'Section 9', 'Section 9 description',
            'https://placekitten.com/200/200', 1, 9),
           (10, 'Section 10', 'Section 10 description',
            'https://placekitten.com/200/200', 1, 10),
           (11, 'Section 11', 'Section 11 description',
            'https://placekitten.com/200/200', 2, 11),
           (12, 'Section 12', 'Section 12 description',
            'https://placekitten.com/200/200', 2, 12),
           (13, 'Section 13', 'Section 13 description',
            'https://placekitten.com/200/200', 2, 13),
           (14, 'Section 14', 'Section 14 description',
            'https://placekitten.com/200/200', 2, 14),
           (15, 'Section 15', 'Section 15 description',
            'https://placekitten.com/200/200', 2, 15),
           (16, 'Section 16', 'Section 16 description',
            'https://placekitten.com/200/200', 2, 16),
           (17, 'Section 17', 'Section 17 description',
            'https://placekitten.com/200/200', 2, 17),
           (18, 'Section 18', 'Section 18 description',
            'https://placekitten.com/200/200', 2, 18),
           (19, 'Section 19', 'Section 19 description',
            'https://placekitten.com/200/200', 3, 19),
           (20, 'Section 20', 'Section 20 description',
            'https://placekitten.com/200/200', 3, 20),
           (21, 'Section 21', 'Section 21 description',
            'https://placekitten.com/200/200', 3, 21),
           (22, 'Section 22', 'Section 22 description',
            'https://placekitten.com/200/200', 3, 22),
           (23, 'Section 23', 'Section 23 description',
            'https://placekitten.com/200/200', 4, 23),
           (24, 'Section 24', 'Section 24 description',
            'https://placekitten.com/200/200', 4, 24),
           (25, 'Section 25', 'Section 25 description',
            'https://placekitten.com/200/200', 4, 25),
           (26, 'Section 26', 'Section 26 description',
            'https://placekitten.com/200/200', 4, 26)
           ]

cursor.executemany(
    'INSERT INTO sections VALUES(?,?,?,?,?,?);', records)

# ACTIVITY

cursor.execute('''DROP TABLE IF EXISTS activities''')

cursor.execute('''CREATE TABLE IF NOT EXISTS activities
             (id INTEGER PRIMARY KEY, raw_html text, section_id integer, question_id integer)''')

records = [(1, '<div>Hello world</div>', 1, 1)]

cursor.executemany(
    'INSERT INTO activities VALUES(?,?,?,?);', records)

# QUESTIONS

cursor.execute('''DROP TABLE IF EXISTS questions''')

cursor.execute('''CREATE TABLE IF NOT EXISTS questions
             (question_id INTEGER PRIMARY KEY, activity_id integer, question_text text, is_active boolean)''')

records = [(1, 1, 'First question text', 1)]

cursor.executemany(
    'INSERT INTO questions VALUES(?,?,?,?);', records)


# QUESTION CHOICES

cursor.execute('''DROP TABLE IF EXISTS choices''')

cursor.execute('''CREATE TABLE IF NOT EXISTS choices
             (choice_id INTEGER PRIMARY KEY, question_id integer, is_correct boolean, choice_text text)''')

records = [(1, 1, 1, 'first choice text'),
           (2, 1, 0, 'second choice text'),
           (3, 1, 0, 'third choice text'),
           (4, 1, 0, 'fourth choice text')]

cursor.executemany(
    'INSERT INTO choices VALUES(?,?,?,?);', records)

print(cursor.lastrowid)


# USER QUESTION ANSWERS - is this needed for this exercise?


connection.commit()

connection.close()
