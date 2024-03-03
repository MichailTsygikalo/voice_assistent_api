from fastapi import APIRouter

router = APIRouter()

@router.get('/monuments')
async def get_all_monuments():
    pass

@router.get('/monument/{description}')
async def get_all_monuments(description:str):
    pass
