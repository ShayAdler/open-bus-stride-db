"""add siri_snapshot.last_heartbeat field

Revision ID: 30d62e479f50
Revises: 67c47a7c2029
Create Date: 2021-11-14 09:46:54.965104+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30d62e479f50'
down_revision = '67c47a7c2029'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('siri_snapshot', sa.Column('last_heartbeat', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('siri_snapshot', 'last_heartbeat')
    # ### end Alembic commands ###
