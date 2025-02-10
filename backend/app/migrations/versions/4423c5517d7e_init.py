"""init

Revision ID: 4423c5517d7e
Revises: c867d955610e
Create Date: 2025-02-07 02:57:43.903111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4423c5517d7e'
down_revision: Union[str, None] = 'c867d955610e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('chat_size', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'chat_size')
    # ### end Alembic commands ###
