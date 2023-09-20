"""Add born_date to persons.

Revision ID: ceff926b3275
Revises: b365249c2d45
Create Date: 2023-09-16 16:05:01.519005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceff926b3275'
down_revision: Union[str, None] = 'b365249c2d45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('born_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('persons', 'born_date')
    # ### end Alembic commands ###
