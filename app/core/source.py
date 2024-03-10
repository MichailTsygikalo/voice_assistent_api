from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine

from core.db import *

async def get_all_monuments(session:AsyncEngine)->list[Monument]:
    result = await session.execute(select(Monument))
    monument = result.scalars().all()
    await session.close()
    return monument

async def get_all_person(session:AsyncEngine)->list[Person]:
    result = await session.execute(select(Person))
    person = result.scalars().all()
    await session.close()
    return person

async def get_person(session:AsyncEngine, id:int)->Optional[Person]:
    result = await session.execute(select(Person).filter(Person.id == id))
    person = result.scalars().first()
    await session.close()
    return person

async def get_monument(session:AsyncEngine, id:int)-> Optional[Monument]:
    result = await session.execute(select(Monument).filter(Monument.id == id))
    monument = result.scalars().first()
    await session.close()
    return monument

async def get_person_d(session:AsyncEngine, description:str)->Optional[Person]:
    result = await session.execute(select(Person).filter(Person.name == description))
    person = result.scalars().first()
    await session.close()
    return person

async def get_monument_d(session:AsyncEngine, description:str)->Optional[Monument]:
    result = await session.execute(select(Monument).filter(Monument.name == description))
    monument = result.scalars().first()
    await session.close()
    return monument

async def get_pers_dataset(session:AsyncEngine)->list[PersonDataset]:
    result = await session.execute(select(PersonDataset))
    person = result.scalars().all()
    await session.close()
    return person

async def get_mon_dataset(session:AsyncEngine)->list[MonumentDataset]:
    result = await session.execute(select(MonumentDataset))
    monument = result.scalars().all()
    await session.close()
    return monument