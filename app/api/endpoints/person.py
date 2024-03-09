from fastapi import APIRouter

from core import get_all_person, get_session
from api.schema import ShowPerson, Person

router = APIRouter()

@router.get('/')
async def get_person()->ShowPerson:
    person = await get_all_person(await get_session())
    person_data = [m.__dict__ for m in person]
    return {'monuments': person_data}

@router.get('/{description}')
async def get_person(description:str)->Person:
    pass
