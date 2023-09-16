"""create_meetingscomments_table

Revision ID: 005
Revises:
Create Date: 2023-09-02

"""

from alembic import op
from sqlalchemy import text

revision = "005"
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, "MeetingsComments"):
        conn.execute(
            text(
                """
            CREATE TABLE MeetingsComments (
               id UUID NOT NULL PRIMARY KEY,
               meeting_id UUID NOT NULL,
               comment_id UUID NOT NULL,
              CONSTRAINT FK_MeetingsComments_meeting_id
                FOREIGN KEY (meeting_id)
                  REFERENCES Meetings(id),
              CONSTRAINT FK_MeetingsComments_comment_id
                FOREIGN KEY (comment_id)
                  REFERENCES Comments(id)
            );
            """
            )
        )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE MeetingsComments")
