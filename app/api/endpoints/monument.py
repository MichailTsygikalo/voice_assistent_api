from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_all_monuments():
    pass

@router.get('/{description}')
async def get_all_monuments(description:str):
    pass
