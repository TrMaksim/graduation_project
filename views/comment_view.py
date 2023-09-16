from datetime import datetime
from http.client import HTTPException

from fastapi import APIRouter, Body, Depends, Form
from sqlalchemy.orm import Session

from controllers.authenticate_controller import get_current_client
from controllers.comment_controller import (create_comments, get_comment_by_id,
                                            get_comments)
from controllers.meeting_controller import (client_connect_to_meeting,
                                            create_meeting, get_meeting_by_id,
                                            get_meetings, patch_meeting)
from dependecies import get_db
from models.models import MeetingsComments
from schemas import Comment, Meeting, TokenData

comments = APIRouter(prefix="/api/comments", tags=["comments"])


@comments.post("/create", response_model=Comment)
def api_create_comment(
    db: Session = Depends(get_db),
    meetings_id: list[str] = Form(),
    comment: str = Form(),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        comment = create_comments(db, meetings_id, comment, current_client.user_id)
        return Comment(
            id=str(comment.id),
            comment=comment.comment,
            client_id=str(comment.client_id),
            create_date=comment.create_date,
            update_date=comment.update_date,
            meetings_id=[
                MeetingsComments(
                    id=str(row.id),
                    comment_id=str(row.comment_id),
                    meeting_id=str(row.meeting_id),
                )
                for row in comment.meetingcomment
            ],
        )
    except HTTPException as e:
        raise e


@comments.get("/all", response_model=list[Comment])
def api_get_comments(
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        comments_from_db = get_comments(db)
        return [
            Comment(
                id=str(comment.id),
                comment=comment.comment,
                client_id=str(comment.client_id),
                create_date=comment.create_date,
                update_date=comment.update_date,
                meetings_id=[
                    MeetingsComments(
                        id=str(row.id),
                        comment_id=str(row.comment_id),
                        meeting_id=str(row.meeting_id),
                    )
                    for row in comment.meetingcomment
                ],
            )
            for comment in comments_from_db
        ]
    except HTTPException as e:
        raise e


@comments.get("/single_comment/{comment_id}", response_model=Comment)
def api_get_comment_by_id(
    comment_id: str,
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        comment = get_comment_by_id(db, comment_id)
        return Comment(
            id=str(comment.id),
            comment=comment.comment,
            client_id=str(comment.client_id),
            create_date=comment.create_date,
            update_date=comment.update_date,
            meetings_id=[
                MeetingsComments(
                    id=str(row.id),
                    comment_id=str(row.comment_id),
                    meeting_id=str(row.meeting_id),
                )
                for row in comment.meetingcomment
            ],
        )
    except HTTPException as e:
        raise e
