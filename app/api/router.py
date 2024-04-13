from fastapi import APIRouter
from api.endpoints import monument_router, person_router, ai_router, page_router

router = APIRouter()

router.include_router(monument_router, tags=['Получить информацию о памятниках'], prefix='/monuments')
router.include_router(person_router, tags=['Получить информацию о личностях'],prefix='/persons')
router.include_router(ai_router, tags=['Запрос к ИИ'],prefix='/ai')
router.include_router(page_router, tags=['Переадресация по голосу'],prefix='/page')