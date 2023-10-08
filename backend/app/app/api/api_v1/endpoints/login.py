from fastapi import APIRouter, Depends
from .....app import schemas, models
from sqlalchemy.orm import session

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(db: session = Depends()):
    pass




