from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine

from core.db import *

async def get_all_monuments(session:AsyncEngine)->list[Monument]:
    result = await session.execute(select(Monument))
    monument = result.scalars().all()
    await session.close()
    return monument

async def get_all_person(session:AsyncEngine)->list[Monument]:
    result = await session.execute(select(Monument))
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
    person = result.scalars().first()
    await session.close()
    return person