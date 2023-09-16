import uuid
from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app

client = TestClient(app)


def test_create_comment():
    meetings_id = [str(uuid.uuid4()), str(uuid.uuid4())]
    comment_text = "Test Comment"

    response = client.post(
        "/api/comments/create",
        json={"meetings_id": meetings_id, "comment": comment_text},
    )

    assert response.status_code == 200
    comment = response.json()
    assert comment["comment"] == comment_text
    assert set(comment["meetings_id"]) == set(meetings_id)


def test_get_comments():
    response = client.get("/api/comments/all")

    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)


def test_get_comment_by_id():
    comment_id = str(uuid.uuid4())

    response = client.get(f"/api/comments/single_comment/{comment_id}")

    assert response.status_code == 200
    comment = response.json()
    assert comment["id"] == comment_id
