from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, DeclarativeMeta, sessionmaker

from config import DB_POSTGRES_HOST, DB_POSTGRES_NAME, DB_POSTGRES_PASSWORD, DB_POSTGRES_PORT, DB_POSTGRES_USERNAME

async_engine = create_async_engine(f'postgresql+asyncpg://{DB_POSTGRES_USERNAME}:{DB_POSTGRES_PASSWORD}@{DB_POSTGRES_HOST}:{DB_POSTGRES_PORT}/{DB_POSTGRES_NAME}')
Base: DeclarativeMeta = declarative_base()
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

class Monument(Base):
    __tablename__ = 'monument'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String, nullable=False) 

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String, nullable=False) 

class Query(Base):
    __tablename__ = 'query'
    id = Column(Integer, primary_key=True)
    request = Column(String, nullable=False)
    response = Column(String, nullable=False)


async def get_session():
    async with async_session() as session:
        return session

