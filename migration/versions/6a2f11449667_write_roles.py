"""write roles

Revision ID: 6a2f11449667
Revises: 05880cf3bdf4
Create Date: 2026-01-30 13:50:47.239830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a2f11449667'
down_revision: Union[str, Sequence[str], None] = '05880cf3bdf4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    roles = sa.table(
        "roles",
        sa.Column("id", sa.Integer),
        sa.Column("name", sa.String())
    )

    op.bulk_insert(
        roles,
        [
            {"name": "admin"},
            {"name": "team-lead"},
            {"name": "project-lead"},
            {"name": "developer"}
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(sa.text(
        """
            DELETE FROM roles WHERE name IN 
            (
                'admin',
                'team-lead',
                'project-lead',
                'developer'
            );
        """
    ))
