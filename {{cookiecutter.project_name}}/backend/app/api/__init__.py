from fastapi import APIRouter

from . import rest


router = APIRouter()

router.include_router(rest.router)
