from app.db.base_class import Base

from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Booking(Base):
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    avg_event_time = Column(Integer, nullable=False)
    start_time = Column(Integer, nullable=False)
    end_time = Column(Integer, nullable=False)
    # Implement Time breaks in schedule here

    create_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text("now()"))
