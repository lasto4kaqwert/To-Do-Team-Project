"""init table

Revision ID: 05880cf3bdf4
Revises: 
Create Date: 2026-01-30 11:24:51.784852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05880cf3bdf4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'roles',
        sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False)
    )
    
    op.create_table(
        'users',
        sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("login", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("role_id", sa.Integer, sa.ForeignKey("roles.id"), nullable=False)
    )

    op.create_table(
        'projects',
        sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False)
    )

    op.create_table(
        'boards',
        sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False)
    )

    op.create_table(
        'teams',
        sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False)
    )

    op.create_table(
        'tasks',
        sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False)
    )

    op.create_table(
        'boards-users',
        sa.Column('id_board', sa.Integer, sa.ForeignKey("boards.id"), nullable=False),
        sa.Column('id_user', sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    )

    op.create_table(
        'boards-projects',
        sa.Column('id_board', sa.Integer, sa.ForeignKey("boards.id"), nullable=False),
        sa.Column('id_project', sa.Integer, sa.ForeignKey("projects.id"), nullable=False)
    )

    op.create_table(
        'boards-tasks',
        sa.Column('id_board', sa.Integer, sa.ForeignKey("boards.id"), nullable=False),
        sa.Column('id_task', sa.Integer, sa.ForeignKey("tasks.id"), nullable=False)
    )

    op.create_table(
        'teams-projects',
        sa.Column('id_team', sa.Integer, sa.ForeignKey("teams.id"), nullable=False),
        sa.Column('id_project', sa.Integer, sa.ForeignKey("projects.id"), nullable=False)
    )

    op.create_table(
        'teams-users',
        sa.Column('id_team', sa.Integer, sa.ForeignKey("teams.id"), nullable=False),
        sa.Column('id_user', sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    
    op.drop_table('teams-users')
    op.drop_table('teams-projects')
    op.drop_table('boards-tasks')
    op.drop_table('boards-projects')
    op.drop_table('boards-users')
    op.drop_table('tasks')
    op.drop_table('projects')
    op.drop_table('boards')
    op.drop_table('users')
    op.drop_table('roles')
