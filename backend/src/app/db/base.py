# Import all the models, so that Base has them before being
# imported by Alembic

from base_class import Base
from ..models.user import User
from ..models.booking import Booking
from ..models.form import Form
from ..models.question import Question
