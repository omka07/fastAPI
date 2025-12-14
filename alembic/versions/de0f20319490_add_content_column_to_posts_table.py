"""add content column to posts table

Revision ID: de0f20319490
Revises: a1b91cc092f7
Create Date: 2025-12-13 22:11:52.527656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de0f20319490'
down_revision: Union[str, Sequence[str], None] = 'a1b91cc092f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
