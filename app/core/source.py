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