from datetime import datetime
from typing import Optional, Union

from pydantic import BaseConfig, BaseModel, Field, validator


class TokenData(BaseModel):
    """
    Schema TokenData.
    """

    user_id: str
    email: str


class Token(BaseModel):
    """
    Schema Token.
    """

    access_token: str
    token_type: str


class BaseDB(BaseModel):
    """
    Schema BaseDB for all schemes working in conjunction with database models.
    """

    id: str
    create_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True


class Client(BaseDB):
    """
    Schema Client.
    """

    username: str
    email: str
    password: str
    phone: str


class ClientMeeting(BaseModel):
    """
    Schema ClientMeeting
    """

    id: str
    client_id: str
    meeting_id: str

    class Config:
        orm_mode = True


class Meeting(BaseDB):
    """
    Schema Meeting.
    """

    place: str
    time_meeting: datetime
    clients: Union[list[ClientMeeting], list]


class ClientPurchase(BaseModel):
    """
    Schema ClientPurchase
    """

    id: str
    client_id: str
    purchase_id: str

    class Config:
        orm_mode = True


class Purchase(BaseDB):
    """
    Schema Purchase.
    """

    purchase_amount: int
    description: str
    clients: Union[list[ClientPurchase], list]


class Debt(BaseModel):
    """
    Schema Debt.
    """

    client_id: str
    amount: float


class MeetingComment(BaseModel):
    """
    Schema MeetingComment.
    """

    id: str
    comment_id: str
    meeting_id: Union[list[Meeting], list]

    class Config:
        orm_mode = True


class Comment(BaseDB):
    """
    Schema Comment.
    """

    comment: str
    client_id: str
