from fastapi import APIRouter
from api.endpoints import monument_router, person_router

router = APIRouter()

router.include_router(monument_router, tags=['Получить информацию о памятниках'])
router.include_router(person_router, tags=['Получить информацию о личностях'])