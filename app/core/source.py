from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import *

async def get_all_monuments(session:AsyncSession)->list[Monument]:
    result = await session.execute(select(Monument))
    monument = result.scalars().all()
    return monument

async def get_all_person(session:AsyncSession)->list[Person]:
    result = await session.execute(select(Person))
    person = result.scalars().all()
    return person

async def get_person(session:AsyncSession, id:int)->Optional[Person]:
    result = await session.execute(select(Person).filter(Person.id == id))
    person = result.scalars().first()
    return person

async def get_monument(session:AsyncSession, id:int)-> Optional[Monument]:
    result = await session.execute(select(Monument).filter(Monument.id == id))
    monument = result.scalars().first()
    return monument

async def get_person_d(session:AsyncSession, description:str)->Optional[Person]:
    result = await session.execute(select(Person).filter(Person.name == description))
    person = result.scalars().first()
    return person

async def get_monument_d(session:AsyncSession, description:str)->Optional[Monument]:
    result = await session.execute(select(Monument).filter(Monument.name == description))
    monument = result.scalars().first()
    return monument

async def get_pers_dataset(session:AsyncSession)->list[PersonDataset]:
    result = await session.execute(select(PersonDataset))
    person = result.scalars().all()
    return person

async def get_mon_dataset(session:AsyncSession)->list[MonumentDataset]:
    result = await session.execute(select(MonumentDataset))
    monument = result.scalars().all()
    return monument