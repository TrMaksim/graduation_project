import uuid
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from controllers.errors_controller import (client_connect_exists_exception,
                                           connect_exists_exception,
                                           connect_not_create_exception,
                                           meeting_exists_exception,
                                           meeting_failed_update,
                                           meeting_not_create_exception,
                                           no_meeting_exception)
from models.models import ClientsMeetings, Meetings


def create_meeting(
    db: Session, place: str, time_meeting: datetime, clients_id: list[str]
) -> type(Meetings):
    try:
        meeting = (
            db.query(Meetings).filter_by(place=place, time_meeting=time_meeting).first()
        )
        if meeting and set(clients_id) in {
            row.client_id for row in meeting.clientmeeting
        }:
            raise meeting_exists_exception
        meeting = Meetings(place=place, time_meeting=time_meeting)

        db.add(meeting)
        db.commit()
        try:
            for client_id in clients_id:
                clientmeeting = ClientsMeetings(
                    client_id=uuid.UUID(client_id), meeting_id=meeting.id
                )
                db.add(clientmeeting)
                db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise meeting_not_create_exception
        return meeting
    except SQLAlchemyError as e:
        db.rollback()
        raise meeting_not_create_exception


def get_meetings(db: Session) -> list[Meetings]:
    return db.query(Meetings).all()


def get_meeting_by_id(db: Session, meeting_id: str) -> type(Meetings):
    meeting = db.query(Meetings).filter_by(id=meeting_id).first()
    if not meeting:
        raise meeting_not_create_exception
    return meeting


def client_connect_to_meeting(
    db: Session, client_id: str, meeting_id: str
) -> ClientsMeetings:
    try:
        meeting = db.query(Meetings).filter_by(id=meeting_id).first()

        if not meeting:
            raise no_meeting_exception
        if (
            db.query(ClientsMeetings)
            .filter_by(client_id=client_id, meeting_id=meeting_id)
            .first()
        ):
            raise client_connect_exists_exception
        client_meeting = ClientsMeetings(client_id=client_id, meeting_id=meeting.id)
        db.add(client_meeting)
        db.commit()
        return client_meeting
    except SQLAlchemyError as e:
        db.rollback()
        raise connect_not_create_exception


def patch_meeting(
    db: Session, meeting_id: str, clients_id_add: list[str]
) -> type(Meetings):
    try:
        clients_id_add = set(clients_id_add)
        meeting = db.query(Meetings).filter_by(id=meeting_id).first()
        if not meeting:
            raise no_meeting_exception
        for client_meeting in meeting.clientmeeting:
            client_id = str(client_meeting.client_id)
            if client_id in clients_id_add:
                clients_id_add.remove(client_id)
        for new_client_id in clients_id_add:
            meeting.clientmeeting.append(
                ClientsMeetings(
                    client_id=uuid.UUID(new_client_id), meeting_id=meeting.id
                )
            )
        db.commit()
        return meeting
    except SQLAlchemyError as e:
        db.rollback()
        raise meeting_failed_update
