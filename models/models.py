from datetime import datetime
from uuid import uuid4

from sqlalchemy import (UUID, Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .db import Base


class Clients(Base):
    __tablename__ = "clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    clientmeeting = relationship("ClientsMeetings", backref="client")
    comment = relationship("Comments", backref="client")
    clientpurchase = relationship("ClientsPurchases", backref="client")


class Meetings(Base):
    __tablename__ = "meetings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    place = Column(String(100), nullable=False)
    time_meeting = Column(DateTime, default=datetime.utcnow)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    clientmeeting = relationship("ClientsMeetings", backref="meeting")
    meetingcomment = relationship("MeetingsComments", backref="meeting")
    purchases = relationship("Purchases", backref="meeting")


class ClientsMeetings(Base):
    __tablename__ = "clientsmeetings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"), default=uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("meetings.id"), default=uuid4)


class Comments(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    comment = Column(String)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"), default=uuid4)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    meetingcomment = relationship("MeetingsComments", backref="comment")


class MeetingsComments(Base):
    __tablename__ = "meetingscomments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    comment_id = Column(UUID(as_uuid=True), ForeignKey("comments.id"), default=uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("meetings.id"), default=uuid4)


class Purchases(Base):
    __tablename__ = "purchases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("meetings.id"), default=uuid4)
    purchase_amount = Column(Integer, nullable=False)
    description = Column(String(30), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    clientpurchase = relationship("ClientsPurchases", backref="purchase")


class ClientsPurchases(Base):
    __tablename__ = "clientspurchases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"), default=uuid4)
    purchases_id = Column(UUID(as_uuid=True), ForeignKey("purchases.id"), default=uuid4)
