from typing import Optional
from fastapi import APIRouter

from core import get_all_monuments, get_session, get_monument
from api.schema import ShowMonument, Monument
from src import monument_ai

router = APIRouter()

@router.get('/',)
async def get_monuments()->ShowMonument:
    monuments = []
    async for session in get_session():
        monuments.extend(await get_all_monuments(session))
    monuments_data = [m.__dict__ for m in monuments]
    return {'monuments': monuments_data}

@router.get('/{id}')
async def get_monuments(id:int)->Optional[Monument]:
    async for session in get_session():
        monument = await get_monument(session, id)
    return monument


@router.get('/ai/{text}')
async def get_monuments(text:str)->Optional[Monument]:
    monument = await monument_ai(text)
    return monument