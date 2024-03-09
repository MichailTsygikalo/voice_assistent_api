from fastapi import APIRouter
from core import get_all_monuments, get_session
from api.schema import ShowMonument, Monument

router = APIRouter()

@router.get('/',)
async def get_monuments()->ShowMonument:
    monuments = await get_all_monuments(await get_session())
    monuments_data = [m.__dict__ for m in monuments]
    return {'monuments':monuments_data}

@router.get('/{description}')
async def get_monuments(description:str)->Monument:
    pass
