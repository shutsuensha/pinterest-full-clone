"""init

Revision ID: e0a109aa32b6
Revises: b6ed0e49b6e8
Create Date: 2024-12-20 15:24:25.333780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0a109aa32b6'
down_revision: Union[str, None] = 'b6ed0e49b6e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'pin_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'pin_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###