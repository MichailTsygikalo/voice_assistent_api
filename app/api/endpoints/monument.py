from typing import Optional
from fastapi import APIRouter

from core import get_all_monuments, get_session, get_monument
from api.schema import ShowMonument, Monument

router = APIRouter()

@router.get('/',)
async def get_monuments()->ShowMonument:
    monuments = await get_all_monuments(await get_session())
    monuments_data = [m.__dict__ for m in monuments]
    return {'monuments':monuments_data}

@router.get('/{id}')
async def get_monuments(id:int)->Optional[Monument]:
    monument = await get_monument(await get_session(), id)
    return monument
