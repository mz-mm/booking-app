"""database revision

Revision ID: 623efb123385
Revises: a1dfb52c89eb
Create Date: 2023-10-15 11:07:59.391332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '623efb123385'
down_revision: Union[str, None] = 'a1dfb52c89eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('avg_event_time', sa.Integer(), nullable=False),
                    sa.Column('start_time', sa.Integer(), nullable=False),
                    sa.Column('end_time', sa.Integer(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('form',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('phone', sa.String(), nullable=True),
                    sa.Column('age', sa.Integer(), nullable=True),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('question',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('phone', sa.String(), nullable=True),
                    sa.Column('age', sa.Integer(), nullable=True),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.String(), server_default=sa.text(
                        'uuid_generate_v4()'), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('full_name', sa.String(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('question')
    op.drop_table('form')
    op.drop_table('booking')
    # ### end Alembic commands ###
