from sqlalchemy.orm import Session

from ...app import schemas
from ...app.core.config import settings
from ...app.db import base


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    pass
