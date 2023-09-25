"""add_users

Revision ID: ca3c39708084
Revises: 4c048ca802f9
Create Date: 2023-09-22 16:42:23.749617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca3c39708084'
down_revision: Union[str, None] = '4c048ca802f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.execute("INSERT INTO users (id, login, password, email, created_at, refresh_token, disabled) VALUES (NULL, 'admin', '$2b$12$BYSC86scFp1ETS7lBH289Ow5T4KQdnWru9J5mBL3Ym274q0wHyg0i', 'admin@localhost', NOW(), NULL, FALSE);")
    op.execute("INSERT INTO users (id, login, password, email, created_at, refresh_token, disabled) VALUES (NULL, 'moder', '$2b$12$F3hxOit5FFOO/IM5oMJWJu71bVVUpzQgM4UKJRDbBZkPl4SNSVcI.', 'moder@localhost', NOW(), NULL, FALSE);")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
