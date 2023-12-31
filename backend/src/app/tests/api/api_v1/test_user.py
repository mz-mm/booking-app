from app import crud
from app.schemas.user import UserCreate
from app.tests.confest import *
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user_new_email(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    full_name = random_lower_string()
    username = random_email()
    password = random_lower_string()

    data = {"full_name": full_name, "email": username, "password": password}
    r = client.post(f"{settings.API_V1_STR}/users/", headers=superuser_token_headers, json=data)

    assert 200 <= r.status_code < 300

    created_user = r.json()
    user = crud.user.get_by_email(db, email=username)

    assert user
    assert user.email == created_user["email"]


def test_get_existing_user(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    full_name = random_lower_string()
    username = random_email()
    password = random_lower_string()

    user_in = UserCreate(email=username, full_name=full_name, password=password)
    user = crud.user.create(db, obj_in=user_in)
    user_id = user.id

    login_data = {
        "username": username,
        "password": password
    }

    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}

    r = client.get(f"{settings.API_V1_STR}/users/{user_id}", headers=headers)

    assert 200 <= r.status_code < 300
    api_user = r.json()
    existing_user = crud.user.get_by_email(db, email=username)
    assert existing_user
    assert existing_user.email == api_user["email"]


def test_create_user_existing_username(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    full_name = random_lower_string()
    username = random_email()
    password = random_lower_string()

    user_in = UserCreate(email=username, full_name=full_name, password=password)
    crud.user.create(db, obj_in=user_in)
    data = {"email": username, "password": password}

    r = client.post(f"{settings.API_V1_STR}/users/", headers=superuser_token_headers, json=data,)
    created_user = r.json()

    assert r.status_code == 400
    assert "_id" not in created_user
