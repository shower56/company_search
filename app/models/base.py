from sqlalchemy import BigInteger, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

LANGUAGE_CHOICES = ["ko", "en", "jp"]


class BaseModel(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
