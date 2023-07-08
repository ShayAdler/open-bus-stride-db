"""modify gtfs_rides_agg_by_hour view

Revision ID: e277ec8f5a04
Revises: eaff3d954883
Create Date: 2023-07-08 15:50:48.706821+00:00

"""
from textwrap import dedent
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = 'e277ec8f5a04'
down_revision = 'eaff3d954883'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("DROP MATERIALIZED VIEW IF EXISTS gtfs_rides_agg_by_hour")
    op.execute(dedent("""
        create materialized view gtfs_rides_agg_by_hour as
        select gtfs_route_id, date_trunc('hour', start_time) as gtfs_route_hour,
                   date_trunc('day', start_time) as gtfs_route_date,
                   count(*) as num_planned_rides,
                   count(*) filter (WHERE sr.scheduled_time_gtfs_ride_id is not null) as num_actual_rides
            from gtfs_ride
            left outer join siri_ride sr on gtfs_ride.id = sr.scheduled_time_gtfs_ride_id
            group by gtfs_route_id, date_trunc('hour', start_time), date_trunc('day', start_time)
    """))
    op.execute("create index idx_gtfs_rides_agg_by_hour_gtfs_route_id on gtfs_rides_agg_by_hour (gtfs_route_id)")
    op.execute("create index idx_gtfs_rides_agg_by_hour_gtfs_route_date on gtfs_rides_agg_by_hour (gtfs_route_hour)")


def downgrade():
    op.execute("drop materialized view if exists gtfs_rides_agg_by_hour")
    op.execute("drop index idx_gtfs_rides_agg_by_hour_gtfs_route_id")
    op.execute("drop index idx_gtfs_rides_agg_by_hour_gtfs_route_date")
