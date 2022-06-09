"""add_indexes_on_ride_start_time_ride_stop_arrival_time

Revision ID: cef897aea9d5
Revises: 7cc970f13408
Create Date: 2022-06-09 17:37:50.484330+00:00

"""
from textwrap import dedent

from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = 'cef897aea9d5'
down_revision = '7cc970f13408'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(dedent("""
        CREATE INDEX idx_gtfs_ride_start_time
        ON gtfs_ride
        (date_trunc('day', start_time))
    """))
    op.execute(dedent("""
        CREATE INDEX idx_gtfs_ride_stop_arrival_time
        ON gtfs_ride_stop
        (date_trunc('day', arrival_time))
    """))


def downgrade():
    op.execute(dedent("""
        DROP INDEX idx_gtfs_ride_start_time
    """))
    op.execute(dedent("""
        DROP INDEX idx_gtfs_ride_stop_arrival_time
    """))
