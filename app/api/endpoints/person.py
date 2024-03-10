from typing import Optional
from fastapi import APIRouter

from core import get_all_person, get_session, get_person
from api.schema import ShowPerson, Person
from src import person_ai

router = APIRouter()

@router.get('/')
async def get_persons()->ShowPerson:
    person = await get_all_person(await get_session())
    person_data = [m.__dict__ for m in person]
    return {'persons': person_data}

@router.get('/{id}')
async def get_persons(id:int)->Optional[Person]:
    person = await get_person(await get_session(), id)
    return person

@router.get('/ai/{text}')
async def get_persons(text:str)->Optional[Person]:
    person = await person_ai(text)
    return person