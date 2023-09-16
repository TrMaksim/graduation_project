"""create_purchase_table

Revision ID: 006
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "006"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "Purchases"):
        conn.execute(
            text(
                """
            CREATE TABLE Purchases (
                id UUID NOT NULL PRIMARY KEY,
                meeting_id UUID NOT NULL,
                purchase_amount INTEGER NOT NULL,
                description VARCHAR(30) NOT NULL,
                create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                CONSTRAINT FK_Purchases_meeting_id
                    FOREIGN KEY (meeting_id)
                    REFERENCES Meetings(id)
            );
            """
            )
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE Purchases")
