import uuid
from datetime import datetime
from typing import Union

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from controllers.errors_controller import (meeting_not_create_exception,
                                           purchase_exists_exception,
                                           purchase_failed_create)
from models.models import ClientsPurchases, Meetings, Purchases


def create_purchase(
    db: Session,
    meeting_id: str,
    purchase_amount: int,
    description: str,
    clients_ids: Union[list[str], None],
):
    try:
        purchase = Purchases(
            meeting_id=meeting_id,
            purchase_amount=purchase_amount,
            description=description,
        )
        db.add(purchase)
        db.commit()

        meeting_clients_ids = {
            str(row.client_id)
            for row in db.query(Meetings).filter_by(id=meeting_id).first().clientmeeting
        }

        if not clients_ids:
            clients_ids = meeting_clients_ids
        else:
            print(clients_ids, meeting_clients_ids)
            clients_ids = set(clients_ids) & meeting_clients_ids

        for client_id in clients_ids:
            purchase.clientpurchase.append(
                ClientsPurchases(client_id=client_id, purchases_id=purchase.id)
            )
        db.commit()
        return purchase

    except SQLAlchemyError as e:
        print(e)
        raise purchase_failed_create


def get_debt(db: Session, meeting_id: str):
    meeting = db.query(Meetings).filter_by(id=meeting_id).first()
    if not meeting:
        raise meeting_not_create_exception
    clients_ids = [row.client_id for row in meeting.clientmeeting]

    clients_debt = dict.fromkeys(clients_ids, 0)

    purchases = meeting.purchases
    for purchase in purchases:
        purchase_clients_ids = [row.client_id for row in purchase.clientpurchase]
        for client_id in purchase_clients_ids:
            clients_debt[client_id] += purchase.purchase_amount / len(
                purchase_clients_ids
            )

    return clients_debt


def get_purchases_this_meeting(db: Session, meeting_id: str):
    meeting = db.query(Meetings).filter_by(id=meeting_id).first()

    if not meeting:
        raise meeting_not_create_exception

    return meeting.purchases
