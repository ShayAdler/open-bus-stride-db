"""add gtfs_rides_agg materialized view

Revision ID: 167517cbecaf
Revises: 7f5f797b8554
Create Date: 2023-02-03 15:23:18.857379+00:00

"""
from textwrap import dedent

from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '167517cbecaf'
down_revision = '7f5f797b8554'
branch_labels = None
depends_on = None

def upgrade():
    op.execute(dedent("""
        create materialized view gtfs_rides_agg_by_hour as
        select a.id as gtfs_route_id, a.hour as gtfs_route_hour, a.total_rides as num_planned_rides, a.actual_rides as num_actual_rides,
               gtfs_route.route_short_name, gtfs_route.route_long_name, gtfs_route.agency_name
        from (
            select gtfs_route_id as id, date_trunc('hour', start_time) as hour, count(*) as total_rides, count(*) filter (WHERE sr.scheduled_time_gtfs_ride_id is not null) as actual_rides
            from gtfs_ride
            left outer join siri_ride sr on gtfs_ride.id = sr.scheduled_time_gtfs_ride_id
            group by gtfs_route_id, date_trunc('hour', start_time)

        ) a, gtfs_route
        where
           a.id=gtfs_route.id
    """))
    op.execute("create index idx_gtfs_rides_agg_by_hour_gtfs_route_id on gtfs_rides_agg_by_hour (gtfs_route_id)")
    op.execute("create index idx_gtfs_rides_agg_by_hour_gtfs_route_date on gtfs_rides_agg_by_hour (gtfs_route_hour)")


def downgrade():
    op.execute("drop materialized view gtfs_rides_agg_by_hour")
    op.execute("drop index idx_gtfs_rides_agg_by_hour_gtfs_route_id")
    op.execute("drop index idx_gtfs_rides_agg_by_hour_gtfs_route_date")
