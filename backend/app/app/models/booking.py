from app.db.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Booking(Base):
    __tablename__ = "form_submissions"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    avg_event_time = Column(InterruptedError, nullable=False)
    start_time = Column(InterruptedError, nullable=False)
    end_time = Column(InterruptedError, nullable=False)
    # Implement Time breaks in schedule here

    create_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text("now()"))
