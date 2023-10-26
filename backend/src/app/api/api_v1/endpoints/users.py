from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud, models
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(*, db: Session = Depends(deps.get_db), user_in: schemas.UserCreate,):

    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)

    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: str, current_user: models.User = Depends(deps.get_current_user), db: Session = Depends(deps.get_db)):

    user = crud.user.get(db, id=user_id)

    if user == current_user:
        return user

    return user
