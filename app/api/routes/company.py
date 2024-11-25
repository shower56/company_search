from typing import List

from fastapi import APIRouter, Header, HTTPException
from sqlalchemy import select, create_engine
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import sessionmaker

from schemas.company import CompanyRequest, TagNameRequest
from models.company import CompanyName, Company, Tag, CompanyTag
from core.config import DATABASE_URL

router = APIRouter()
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, autocommit=False)
db = SessionLocal()


@router.get("/companies/{company_name}")
async def get_company(company_name: str, x_wanted_language: str = Header(...)):
    query = (
        select(Company)
        .join(CompanyName)
        .filter(CompanyName.name == company_name)
        .options(
            joinedload(Company.company_names),
            joinedload(Company.company_tags)
            .joinedload(CompanyTag.tag)
            .joinedload(Tag.tag_names),
        )
    )
    result = db.execute(query).scalars().all()

    if not result:
        raise HTTPException(status_code=404)
    return result


router = APIRouter()


@router.get("/search")
async def search_company(query: str, x_wanted_language: str = Header(...)):
    query = select(
        CompanyName
    ).filter(
        CompanyName.language_code==x_wanted_language
    ).filter(
        CompanyName.name.ilike(f"%{query}%")
    ).order_by(CompanyName.name)
    result = db.execute(query).scalars().all()

    return [{"company_name": company.name} for company in result]


@router.post("/companies")
async def create_company(company: CompanyRequest, x_wanted_language: str = Header(...)):
    return {}


@router.get("/tags")
async def search_by_tag(query: str, x_wanted_language: str = Header(...)):
    return []


@router.put("/companies/{company_name}/tags")
async def add_company_tags(company_name: str, tags: List[TagNameRequest], x_wanted_language: str = Header(...)):
    return {}


@router.delete("/companies/{company_name}/tags/{tag_name}")
async def delete_company_tag(company_name: str, tag_name: str, x_wanted_language: str = Header(...)):
    return {}
