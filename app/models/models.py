from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()

questions = Table(
    'questions',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('question', String),
    Column('answer', String),
    Column('created_at', TIMESTAMP),
)

