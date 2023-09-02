from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy import Column, UUID, String, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from sqlalchemy import create_engine

engine = create_engine("postgresql://maksym:123456@localhost/graduation_db")
Base = declarative_base()


class Client(Base):
    __tablename__ = "Clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(36), nullable=False)
    phone = Column(String(20), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    clientmeeting = relationship("ClientsMeetings", backref="client")
    comment = relationship("Comments", backref="client")
    clientpurchase = relationship("ClientsPurchases", backref="client")


class Meeting(Base):
    __tablename__ = "Meetings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    place = Column(String(100), nullable=False)
    time_meeting = Column(DateTime, default=datetime.utcnow)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    clientmeeting = relationship("ClientsMeetings", backref="meeting")
    meetingcomment = relationship("MeetingsComments", backref="meeting")


class ClientMeeting(Base):
    __tablename__ = "ClientsMeetings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("Clients.id"), default=uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("Meetings.id"), default=uuid4)


class Comment(Base):
    __tablename__ = "Comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    comment = Column(String)
    client_id = Column(UUID(as_uuid=True), ForeignKey("Clients.id"), default=uuid4)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    meetingcomment = relationship("MeetingsComments", backref="comment")


class MeetingComment(Base):
    __tablename__ = "MeetingsComments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    comment_id = Column(UUID(as_uuid=True), ForeignKey("Comments.id"), default=uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("Meetings.id"), default=uuid4)


class Purchase(Base):
    __tablename__ = "Purchases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    purchase_amount = Column(Integer, nullable=False)
    description = Column(String(30), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    clientpurchase = relationship("ClientsPurchases", backref="purchase")


class ClientPurchase(Base):
    __tablename__ = "ClientsPurchases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("Clients.id"), default=uuid4)
    purchase_id = Column(UUID(as_uuid=True), ForeignKey("Purchases.id"), default=uuid4)


Base.metadata.create_all(engine)
