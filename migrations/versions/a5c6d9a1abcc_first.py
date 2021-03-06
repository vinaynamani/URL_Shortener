"""FIRST

Revision ID: a5c6d9a1abcc
Revises: 
Create Date: 2021-10-29 18:56:34.846597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5c6d9a1abcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urltable',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('short_url', sa.String(length=100), nullable=True),
    sa.Column('long_url', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urltable')
    # ### end Alembic commands ###
