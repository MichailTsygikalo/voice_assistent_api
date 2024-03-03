from fastapi import APIRouter

router = APIRouter()

@router.get('/persons')
async def get_all_person():
    pass

@router.get('/person/{description}')
async def get_person(id:str):
    pass
