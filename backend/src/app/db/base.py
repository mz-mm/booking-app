# Import all the models, so that Base has them before being imported by Alembic

from app.db.base_class import Base

from app.models.user import User
from app.models.booking import Booking
from app.models.form import Form
from app.models.question import Question
