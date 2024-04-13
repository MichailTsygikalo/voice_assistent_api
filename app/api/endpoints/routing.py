from fastapi import APIRouter

from src import page

router = APIRouter()

@router.get('/{text}')
async def get(text:str):
    return await page(text)