from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session

from controllers.authenticate_controller import (authenticate_client,
                                                 create_access_token,
                                                 get_current_client,
                                                 register_client)
from dependecies import get_db
from schemas import Token, TokenData

clients = APIRouter(prefix="/api/clients", tags=["clients"])


@clients.post("/login", response_model=Token)
def api_login(
    db: Session = Depends(get_db), email: str = Form(), password: str = Form()
):
    """
    Endpoint for client authorization.
     :param db: DB session.
     :param email: Client's email.
     :param password: Password.
     :return: The result of the corresponding method.
    """
    try:
        client = authenticate_client(db, email, password)
        access_token = create_access_token(
            data={"client_id": str(client.id), "email": client.email}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e


@clients.post("/register", response_model=Token)
def api_register(
    db: Session = Depends(get_db),
    email: str = Form(),
    password: str = Form(),
    repeat_password: str = Form(),
    phone: str = Form(),
    username: str = Form(),
):
    """
    Endpoint for client registration.
     :param db: DB session.
     :param email: Email.
     :param password: Password.
     :param repeat_password: Password again.
     :return: The result of the corresponding method.
    """
    try:
        client = register_client(db, email, password, repeat_password, username, phone)
        access_token = create_access_token(
            data={"user_id": str(client.id), "email": client.email}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e


@clients.get("/me", response_model=TokenData)
def api_me(current_client: TokenData = Depends(get_current_client)):
    """
    Endpoint for getting the current client.
    :param current_client: Current client.
    :return: The result of the corresponding method.
    """
    return current_client
