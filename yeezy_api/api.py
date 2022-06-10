from fastapi import APIRouter
from yeezy_api.endpoints import quote

router = APIRouter()

router.include_router(quote.router, tags=['quote generator'])
