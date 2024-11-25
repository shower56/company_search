from fastapi import APIRouter

from api.routes import company, docs

router = APIRouter()
router.include_router(company.router, tags=["company"], prefix="/v1")
router.include_router(docs.router, tags=["docs"], prefix="/v1")
