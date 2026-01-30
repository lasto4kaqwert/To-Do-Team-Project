"""create admin

Revision ID: e4a76f531f93
Revises: 6a2f11449667
Create Date: 2026-01-30 13:58:13.452363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4a76f531f93'
down_revision: Union[str, Sequence[str], None] = '6a2f11449667'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()

    roles = sa.table(
        "roles",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String)
    )

    users = sa.table(
        "users",
        sa.column("id", sa.Integer),
        sa.column("username", sa.String),
        sa.column("login", sa.String),
        sa.column("password", sa.String),
        sa.column("role_id", sa.Integer)
    )

    admin_role_id = conn.execute(
        sa.select(roles.c.id).where(roles.c.name == "admin")
    ).scalar_one()

    exists = conn.execute(
        sa.text("SELECT 1 FROM users WHERE login = 'admin'")
    ).scalar()

    if not exists:
        conn.execute(
            sa.insert(users).values(
                username="Администратор",
                login="admin",
                password="admin",
                role_id=admin_role_id,
            )
        )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(sa.text("DELETE FROM users WHERE login = 'admin'"))
