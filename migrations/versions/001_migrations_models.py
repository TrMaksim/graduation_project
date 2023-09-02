"""create_clients_table

Revision ID: 001
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "001"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "Сlients"):
        conn.execute(text(
            '''
            CREATE TABLE Сlients (
                id UUID NOT NULL, 
                username VARCHAR(50) NOT NULL, 
                email VARCHAR(255) NOT NULL, 
                password VARCHAR(36) NOT NULL, 
                phone VARCHAR(20) NOT NULL, 
                create_date TIMESTAMP NOT NULL, 
                update_date TIMESTAMP NOT NULL
            )
            '''
            )
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE Clients")
