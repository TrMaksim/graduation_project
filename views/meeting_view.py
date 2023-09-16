from datetime import datetime
from http.client import HTTPException

from fastapi import APIRouter, Body, Depends, Form
from sqlalchemy.orm import Session

from controllers.authenticate_controller import get_current_client
from controllers.meeting_controller import (client_connect_to_meeting,
                                            create_meeting, get_meeting_by_id,
                                            get_meetings, patch_meeting)
from dependecies import get_db
from schemas import ClientMeeting, Meeting, TokenData

meetings = APIRouter(prefix="/api/meetings", tags=["meetings"])


@meetings.post("/create", response_model=Meeting)
def api_create_meeting(
    db: Session = Depends(get_db),
    place: str = Form(),
    time_meeting: datetime = Form(),
    clients_id: list[str] = Form(),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        meeting = create_meeting(db, place, time_meeting, clients_id)
        return Meeting(
            id=str(meeting.id),
            place=meeting.place,
            time_meeting=meeting.time_meeting,
            create_date=meeting.create_date,
            update_date=meeting.update_date,
            clients=[
                ClientMeeting(
                    id=str(row.id),
                    client_id=str(row.client_id),
                    meeting_id=str(row.meeting_id),
                )
                for row in meeting.clientmeeting
            ],
        )
    except HTTPException as e:
        raise e


@meetings.get("/all", response_model=list[Meeting])
def api_get_meetings(
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        meetings_from_db = get_meetings(db)
        return [
            Meeting(
                id=str(meeting.id),
                place=meeting.place,
                time_meeting=meeting.time_meeting,
                create_date=meeting.create_date,
                update_date=meeting.update_date,
                clients=[
                    ClientMeeting(
                        id=str(row.id),
                        client_id=str(row.client_id),
                        meeting_id=str(row.meeting_id),
                    )
                    for row in meeting.clientmeeting
                ],
            )
            for meeting in meetings_from_db
        ]
    except HTTPException as e:
        raise e


@meetings.get("/single_meeting/{meeting_id}", response_model=Meeting)
def api_get_meeting_by_id(
    meeting_id: str,
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        meeting = get_meeting_by_id(db, meeting_id)
        return Meeting(
            id=str(meeting.id),
            place=meeting.place,
            time_meeting=meeting.time_meeting,
            create_date=meeting.create_date,
            update_date=meeting.update_date,
            clients=[
                ClientMeeting(
                    id=str(row.id),
                    client_id=str(row.client_id),
                    meeting_id=str(row.meeting_id),
                )
                for row in meeting.clientmeeting
            ],
        )
    except HTTPException as e:
        raise e


@meetings.post("/connect", response_model=ClientMeeting)
def api_connect_client_to_meeting(
    meeting_id: str = Form(),
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        connect = client_connect_to_meeting(db, current_client.user_id, meeting_id)
        return ClientMeeting(
            id=str(connect.id),
            client_id=str(connect.client_id),
            meeting_id=str(connect.meeting_id),
        )
    except HTTPException as e:
        raise e


@meetings.patch("/update", response_model=Meeting)
def api_update_meeting(
    db: Session = Depends(get_db),
    meeting_id: str = Form(),
    clients_id_add: list[str] = Form(),
):
    try:
        update_meeting = patch_meeting(db, meeting_id, clients_id_add)
        return Meeting(
            id=str(update_meeting.id),
            place=update_meeting.place,
            time_meeting=update_meeting.time_meeting,
            create_date=update_meeting.create_date,
            update_date=update_meeting.update_date,
            clients=[
                ClientMeeting(
                    id=str(row.id),
                    client_id=str(row.client_id),
                    meeting_id=str(row.meeting_id),
                )
                for row in update_meeting.clientmeeting
            ],
        )
    except HTTPException as e:
        raise e
