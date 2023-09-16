from datetime import datetime
from http.client import HTTPException
from typing import Union

from fastapi import APIRouter, Body, Depends, Form
from sqlalchemy.orm import Session

from controllers.authenticate_controller import get_current_client
from controllers.meeting_controller import (client_connect_to_meeting,
                                            create_meeting, get_meeting_by_id,
                                            get_meetings, patch_meeting)
from controllers.purchase_controller import (create_purchase, get_debt,
                                             get_purchases_this_meeting)
from dependecies import get_db
from schemas import (ClientMeeting, ClientPurchase, Debt, Meeting, Purchase,
                     TokenData)

purchases = APIRouter(prefix="/api/purchases", tags=["purchases"])


@purchases.post("/make_purchase", response_model=Purchase)
def api_create_purchase(
    db: Session = Depends(get_db),
    meeting_id: str = Form(),
    purchase_amount: int = Form(),
    description: str = Form(),
    clients_ids: list[str] = Form(None),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        purchase = create_purchase(
            db, meeting_id, purchase_amount, description, clients_ids
        )
        return Purchase(
            id=str(purchase.id),
            purchase_amount=purchase.purchase_amount,
            description=purchase.description,
            create_date=purchase.create_date,
            update_date=purchase.update_date,
            clients=[
                ClientPurchase(
                    id=str(row.id),
                    client_id=str(row.client_id),
                    purchase_id=str(row.purchases_id),
                )
                for row in purchase.clientpurchase
            ],
        )
    except HTTPException as e:
        raise e


@purchases.get("/from_meeting/{meeting_id}", response_model=list[Purchase])
def api_get_purchase(
    meeting_id: str,
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        purchases = get_purchases_this_meeting(db, meeting_id)
        return [
            Purchase(
                id=str(purchase.id),
                purchase_amount=purchase.purchase_amount,
                description=purchase.description,
                create_date=purchase.create_date,
                update_date=purchase.update_date,
                clients=[
                    ClientPurchase(
                        id=str(row.id),
                        client_id=str(row.client_id),
                        purchase_id=str(row.purchases_id),
                    )
                    for row in purchase.clientpurchase
                ],
            )
            for purchase in purchases
        ]
    except HTTPException as e:
        raise e


@purchases.get("/debt/{meeting_id}", response_model=list[Debt])
def api_get_debt(
    meeting_id: str,
    db: Session = Depends(get_db),
    current_client: TokenData = Depends(get_current_client),
):
    try:
        debts = get_debt(db, meeting_id)
        return [
            Debt(client_id=str(client_id), amount=amount)
            for client_id, amount in debts.items()
        ]
    except HTTPException as e:
        raise e
