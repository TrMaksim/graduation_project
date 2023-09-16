import uuid
from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app

client = TestClient(app)


def test_create_meeting():
    place = "Test Place"
    time_meeting = datetime.now()
    clients_id = [str(uuid.uuid4()), str(uuid.uuid4())]

    response = client.post(
        "/api/meetings/create",
        json={
            "place": place,
            "time_meeting": time_meeting.isoformat(),
            "clients_id": clients_id,
        },
    )

    assert response.status_code == 200
    meeting = response.json()
    assert meeting["place"] == place
    assert meeting["time_meeting"] == time_meeting.isoformat()


def test_get_meetings():
    response = client.get("/api/meetings/all")

    assert response.status_code == 200
    meetings = response.json()
    assert isinstance(meetings, list)


def test_get_meeting_by_id():
    meeting_id = str(uuid.uuid4())

    response = client.get(f"/api/meetings/single_meeting/{meeting_id}")

    assert response.status_code == 200
    meeting = response.json()
    assert meeting["id"] == meeting_id


def test_client_connect_to_meeting():
    meeting_id = str(uuid.uuid4())
    client_id = str(uuid.uuid4())

    response = client.post(
        "/api/meetings/connect",
        json={"meeting_id": meeting_id},
    )

    assert response.status_code == 200
    client_meeting = response.json()
    assert client_meeting["meeting_id"] == meeting_id


def test_patch_meeting():
    meeting_id = str(uuid.uuid4())
    clients_id_add = [str(uuid.uuid4()), str(uuid.uuid4())]

    response = client.patch(
        "/api/meetings/update",
        json={"meeting_id": meeting_id, "clients_id_add": clients_id_add},
    )

    assert response.status_code == 200
    updated_meeting = response.json()
    assert updated_meeting["id"] == meeting_id
