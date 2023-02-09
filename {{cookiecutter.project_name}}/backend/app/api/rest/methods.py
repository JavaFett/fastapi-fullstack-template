from fastapi import APIRouter


router = APIRouter()


@router.post('/method1')
def method1(
):
    """Method1 descriptions"""
    return


@router.get('/method2')
def method2(
):
    """Method2 descriptions"""
    return
