from fastapi import APIRouter

from . import methods


router = APIRouter(prefix='/rest', tags=['rest'])

router.include_router(methods.router)
