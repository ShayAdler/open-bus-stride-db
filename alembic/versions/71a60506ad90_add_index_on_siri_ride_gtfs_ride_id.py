"""add_index_on_siri_ride_gtfs_ride_id

Revision ID: 71a60506ad90
Revises: c0fa93cfbf95
Create Date: 2022-11-21 18:48:02.929521+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '71a60506ad90'
down_revision = 'c0fa93cfbf95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_siri_ride_route_gtfs_ride_id'), 'siri_ride', ['route_gtfs_ride_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_siri_ride_route_gtfs_ride_id'), table_name='siri_ride')
    # ### end Alembic commands ###
