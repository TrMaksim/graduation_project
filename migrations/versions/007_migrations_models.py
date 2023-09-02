"""create_clientspuschases_table

Revision ID: 007
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "007"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "ClientsPurchases"):
        conn.execute(text(
            """
            CREATE TABLE ClientsPurchases (
               id UUID NOT NULL,
               client_id UUID NOT NULL,
               purchase_id UUID NOT NULL,
              CONSTRAINT FK_ClientsPurchases
                FOREIGN KEY ("client_id")
                  REFERENCES Сlients("id"),
              CONSTRAINT FK_ClientsPurchases
                FOREIGN KEY ("purchase_id")
                  REFERENCES Purchase("id")
            );
            """)
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE ClientsPuschases")
