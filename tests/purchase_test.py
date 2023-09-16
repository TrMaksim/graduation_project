import uuid
from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app

client = TestClient(app)


def test_create_purchase():
    meeting_id = str(uuid.uuid4())
    purchase_amount = 100
    description = "Test Purchase"
    clients_ids = [str(uuid.uuid4()), str(uuid.uuid4())]

    response = client.post(
        "/api/purchases/make_purchase",
        json={
            "meeting_id": meeting_id,
            "purchase_amount": purchase_amount,
            "description": description,
            "clients_ids": clients_ids,
        },
    )

    assert response.status_code == 200
    purchase = response.json()
    assert purchase["meeting_id"] == meeting_id
    assert purchase["purchase_amount"] == purchase_amount


def test_get_purchases_this_meeting():
    meeting_id = str(uuid.uuid4())

    response = client.get(f"/api/purchases/from_meeting/{meeting_id}")

    assert response.status_code == 200
    purchases = response.json()
    assert isinstance(purchases, list)


def test_get_debt():
    meeting_id = str(uuid.uuid4())

    response = client.get(f"/api/purchases/debt/{meeting_id}")

    assert response.status_code == 200
    debts = response.json()
    assert isinstance(debts, list)
