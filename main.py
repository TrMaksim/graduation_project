from fastapi import FastAPI

from views.client_view import clients
from views.comment_view import comments
from views.meeting_view import meetings
from views.purchase_view import purchases

app = FastAPI()

app.include_router(clients)
app.include_router(meetings)
app.include_router(purchases)
app.include_router(comments)
