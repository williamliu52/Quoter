"""empty message

Revision ID: 356e2246d059
Revises: 
Create Date: 2017-03-03 19:40:37.533412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356e2246d059'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
    sa.Column('symbol', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('symbol'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('symbol')
    )
    op.create_table('quotes',
    sa.Column('symbol', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('change', sa.Float(), nullable=True),
    sa.Column('changePercent', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.String(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('changeYTD', sa.Float(), nullable=True),
    sa.Column('changeYTDPercent', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('open', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['symbol'], ['stocks.name'], ),
    sa.PrimaryKeyConstraint('symbol'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('symbol')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotes')
    op.drop_table('stocks')
    # ### end Alembic commands ###
