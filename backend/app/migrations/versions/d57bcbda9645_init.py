"""init

Revision ID: d57bcbda9645
Revises: c6b44dff29df
Create Date: 2024-12-22 10:58:18.189027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd57bcbda9645'
down_revision: Union[str, None] = 'c6b44dff29df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pins', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pins', 'is_active')
    # ### end Alembic commands ###
