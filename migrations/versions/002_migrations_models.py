"""create_meetings_table

Revision ID: 002
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "002"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "Meetings"):
        conn.execute(
            text(
                """
            CREATE TABLE Meetings (
               id UUID NOT NULL,
               place VARCHAR(100) NOT NULL,
               time_meeting timestamp NOT NULL,
               create_date timestamp NOT NULL,
               update_date timestamp NOT NULL,
            )
            """
            )
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE Meetings")
