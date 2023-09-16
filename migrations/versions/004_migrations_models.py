"""create_comments_table

Revision ID: 004
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "004"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "Comments"):
        conn.execute(
            text(
                """
            CREATE TABLE Comments (
               id UUID NOT NULL PRIMARY KEY,
               comment TEXT NOT NULL,
               client_id UUID NOT NULL,
               update_date TIMESTAMP NOT NULL,
               create_date TIMESTAMP NOT NULL,
              CONSTRAINT FK_Comments_client_id
                FOREIGN KEY (client_id)
                  REFERENCES Clients(id)
                );
            """
            )
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE Comments")
