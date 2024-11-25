from typing import List, Optional, Dict
from pydantic import BaseModel, ConfigDict, Field


class CompanyNameRequest(BaseModel):
    ko: Optional[str] = Field(default=None)
    en: Optional[str] = Field(default=None)
    ja: Optional[str] = Field(default=None)
    tw: Optional[str] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)


class TagNameRequest(BaseModel):
    tag_name: Dict[str, str]

    model_config = ConfigDict(from_attributes=True)


class CompanyRequest(BaseModel):
    company_name: CompanyNameRequest
    tags: List[TagNameRequest]

    model_config = ConfigDict(from_attributes=True)


class CompanyResponse(BaseModel):
    company_name: str
    tags: List[str] = []

    model_config = ConfigDict(from_attributes=True)
