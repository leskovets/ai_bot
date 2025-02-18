"""empty message

Revision ID: 145553a347a5
Revises: 
Create Date: 2024-08-08 16:57:35.014051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '145553a347a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('treads',
    sa.Column('chat_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('tread_id', sa.Integer(), nullable=True),
    sa.Column('key_value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('chat_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('treads')
    # ### end Alembic commands ###
