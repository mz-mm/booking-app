import uuid
from app.db.db import Base
from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=str(uuid.uuid4()),
                server_default=text("uuid_generate_v4()"), unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text("now()"))
