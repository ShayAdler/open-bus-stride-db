"""add gtfs_rides_agg_by_hour index

Revision ID: 7e9880e6fcf6
Revises: e277ec8f5a04
Create Date: 2023-07-26 18:26:56.115750+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '7e9880e6fcf6'
down_revision = 'e277ec8f5a04'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("create index idx_gtfs_rides_agg_by_hour_gtfs_route_date_2 on gtfs_rides_agg_by_hour (gtfs_route_date)")


def downgrade():
    op.execute("drop index idx_gtfs_rides_agg_by_hour_gtfs_route_date_2")
