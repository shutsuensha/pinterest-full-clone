"""init

Revision ID: 64921018d529
Revises: 1a6a34904b30
Create Date: 2025-02-06 20:58:27.788465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64921018d529'
down_revision: Union[str, None] = '1a6a34904b30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('chat_color', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'chat_color')
    # ### end Alembic commands ###
