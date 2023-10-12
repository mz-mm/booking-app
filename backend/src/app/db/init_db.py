from sqlalchemy.orm import Session

from app.db.session import engine
from app.db.base_class import Base


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
