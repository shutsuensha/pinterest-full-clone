"""init

Revision ID: 46efc63fda1c
Revises: 635b21238749
Create Date: 2024-12-21 15:39:01.093359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46efc63fda1c'
down_revision: Union[str, None] = '635b21238749'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pins', sa.Column('rgb', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pins', 'rgb')
    # ### end Alembic commands ###
