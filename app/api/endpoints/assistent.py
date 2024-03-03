from fastapi import APIRouter

from src import ai

router = APIRouter()

@router.get('/{text}')
async def get_answer(text:str):
    return ai(text)