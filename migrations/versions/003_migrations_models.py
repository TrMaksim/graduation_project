"""create_clientsmeetings_table

Revision ID: 003
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "003"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "ClientsMeetings"):
        conn.execute(text(
            """
            CREATE TABLE ClientsMeetings (
               id UUID NOT NULL,
               client_id UUID NOT NULL,
               meeting_id UUID NOT NULL,
              CONSTRAINT FK_ClientsMeetings.client_id
                FOREIGN KEY ("client_id")
                  REFERENCES Сlients("id"),
              CONSTRAINT FK_ClientsMeetings.meeting_id
                FOREIGN KEY ("meeting_id")
                  REFERENCES Meetings("id")
            );
            """)
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE ClientsMeetings")
