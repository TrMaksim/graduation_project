import uuid
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from controllers.errors_controller import (comment_exists_exception,
                                           comment_not_create_exception,
                                           comment_not_found_exception)
from models.models import Comments, Meetings, MeetingsComments


def create_comments(
    db: Session, meetings_id: list[str], comment: str, client_id: str
) -> type(Comments):
    try:
        comments = (
            db.query(Comments).filter_by(comment=comment, client_id=client_id).first()
        )
        if comments and set(meetings_id) in {
            row.meeting_id for row in comments.meetingcomment
        }:
            raise comment_exists_exception
        comments = Comments(comment=comment, client_id=client_id)

        db.add(comments)
        db.commit()
        try:
            for meeting_id in meetings_id:
                meetingcomment = MeetingsComments(
                    meeting_id=uuid.UUID(meeting_id), comment_id=comments.id
                )
                db.add(meetingcomment)
                db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise comment_not_create_exception
        return comments
    except SQLAlchemyError as e:
        db.rollback()
        raise comment_not_create_exception


def get_comments(db: Session) -> list[Comments]:
    return db.query(Comments).filter_by().all()


def get_comment_by_id(db: Session, comment_id: str) -> type(Comments):
    comment = db.query(Comments).filter_by(id=comment_id).first()
    if not comment:
        raise comment_not_create_exception
    return comment
