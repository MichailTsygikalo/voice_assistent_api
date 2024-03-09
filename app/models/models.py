from sqlalchemy import Integer, MetaData, String, Table, Column

metadata = MetaData()

query = Table(
    'query',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('request',String,nullable=False),
    Column('response',String,nullable=False)
)

person = Table(
    'person',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String,nullable=False),
    Column('description',String,nullable=False),
    Column('photo',String,nullable=False)
)

monument = Table(
    'monument',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String,nullable=False),
    Column('description',String,nullable=False),
    Column('photo',String,nullable=False)
)

