from app.db.base_class import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    age = Column(Integer, nullable=True)

    create_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text("now()"))
