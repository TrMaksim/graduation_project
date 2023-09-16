from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from config import ALGORITHM, SECRET_KEY
from controllers.errors_controller import (passwords_match_exception,
                                           user_exists_exception,
                                           user_not_create_exception,
                                           user_not_found_exception,
                                           wrong_credentials_exception,
                                           wrong_password_exception,
                                           wrong_token_exception)
from models.models import Clients
from schemas import Client as ClientSchema
from schemas import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password: str, hashed_password: str):
    """
    Method for checking the password.
     :param plain_password: Password without encryption.
     :param hashed_password: Encrypted password.
     :return: Password verification result.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """
    Password encryption method.
     :param password: Password without encryption.
     :return: The result of password encryption.
    """
    return pwd_context.hash(password)


def get_user(db: Session, email: str):
    """
    Method for obtaining a user from the database by mail.
     :param db: DB session.
     :param email: Email.
     :return: Result of type Users.
    """
    if user := db.query(Clients).filter_by(email=email).first():
        return ClientSchema(
            id=str(user.id),
            username=user.username,
            email=user.email,
            password=user.password,
            phone=user.phone,
            create_date=user.create_date,
            update_date=user.update_date,
        )


def authenticate_client(db: Session, email: str, password: str):
    """
    Method for user authentication.
     :param db: DB session.
     :param email: Email.
     :param password: Password.
     :return: Authorization error or user type Users.
    """
    user = get_user(db, email)
    if not user:
        raise user_not_found_exception
    if not verify_password(password, user.password):
        raise wrong_password_exception
    return user


def register_client(
    db: Session,
    email: str,
    password: str,
    repeat_password: str,
    phone: str,
    username: str,
):
    """
    Method for registering a user.
     :param db: DB session.
     :param email: Email.
     :param password: Password.
     :param repeat_password: Password again.
     :return: Registration error or user type Users.
    """
    user = get_user(db, email)
    if not user:
        if password != repeat_password:
            raise passwords_match_exception
        new_user = Clients(
            username=username,
            email=email,
            password=get_password_hash(password),
            phone=phone,
        )
        try:
            db.add(new_user)
            db.commit()
            return new_user
        except SQLAlchemyError as e:
            print(e)
            db.rollback()
            # return False
            raise user_not_create_exception
    raise user_exists_exception


def create_access_token(data: dict):
    """
    Method for creating a user token.
     :param data: Data to add to the token.
     :return: Token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=365)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_client(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Method for getting the current user.
    :param token: User token.
    :return: Error or current user.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        client_id = payload.get("client_id")
        email = payload.get("email")
        if not email or not client_id:
            raise wrong_credentials_exception
        token_data = TokenData(user_id=client_id, email=email)
        return token_data
    except JWTError:
        raise wrong_token_exception
