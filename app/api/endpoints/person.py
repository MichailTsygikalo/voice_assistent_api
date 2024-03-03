from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_all_person():
    pass

@router.get('/{description}')
async def get_person(description:str):
    pass
