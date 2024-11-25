from sqlalchemy import BigInteger, Column, Enum, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base import BaseModel, LANGUAGE_CHOICES


class Company(BaseModel):
    __tablename__ = "companies_company"
    company_names = relationship("CompanyName", back_populates="company")
    company_tags = relationship("CompanyTag", back_populates="company")


class CompanyName(BaseModel):
    __tablename__ = "company_name"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    company_id = Column(BigInteger, ForeignKey("company.id"), nullable=False)
    name = Column(String(100), nullable=False)
    language_code = Column(Enum(*LANGUAGE_CHOICES), nullable=False)
    company = relationship("Company", back_populates="company_names")


class CompanyTag(BaseModel):
    __tablename__ = "companies_tag"

    company_id = Column(BigInteger, ForeignKey("company.id"))
    tag_id = Column(BigInteger, ForeignKey("tag.id"))
    company = relationship("Company", back_populates="company_tags")
    tag = relationship("Tag", back_populates="company_tags")


class Tag(BaseModel):
    __tablename__ = "tags_tag"

    tag_names = relationship("TagName", back_populates="tag")
    company_tags = relationship("CompanyTag", back_populates="tag")


class TagName(BaseModel):
    __tablename__ = "tags_name"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    tag_id = Column(BigInteger, ForeignKey("tag.id"), nullable=False)
    name = Column(String(127), nullable=False)
    language_code = Column(Enum(*LANGUAGE_CHOICES), nullable=False)
    tag = relationship("Tag", back_populates="tag_names")