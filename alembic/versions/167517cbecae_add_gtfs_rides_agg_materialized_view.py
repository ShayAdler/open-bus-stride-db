"""add gtfs_rides_agg materialized view

Revision ID: 167517cbecae
Revises: 7f5f797b8553
Create Date: 2023-02-03 15:23:18.857379+00:00

"""
from textwrap import dedent

from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '167517cbecae'
down_revision = '7f5f797b8553'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(dedent("""
        create materialized view gtfs_rides_agg as
        select a.id as gtfs_route_id, a.day as gtfs_route_date, a.cnt as num_planned_rides, b.cnt as num_actual_rides
        from (
            select gtfs_route_id as id, date_trunc('day', start_time + INTERVAL '4 HOURS') as day, count(1) as cnt
            from gtfs_ride
            group by gtfs_route_id, date_trunc('day', start_time + INTERVAL '4 HOURS')
        ) a,
        (
            select gtfs_ride.gtfs_route_id as id, date_trunc('day', gtfs_ride.start_time + INTERVAL '4 HOURS') as day, count(1) as cnt
            from gtfs_ride, siri_ride
            where siri_ride.gtfs_ride_id = gtfs_ride.id
            group by gtfs_ride.gtfs_route_id, date_trunc('day', gtfs_ride.start_time + INTERVAL '4 HOURS')
        ) b
        where a.id = b.id and a.day = b.day
    """))
    op.execute("create index idx_gtfs_rides_agg_gtfs_route_id on gtfs_rides_agg (gtfs_route_id)")
    op.execute("create index idx_gtfs_rides_agg_gtfs_route_date on gtfs_rides_agg (gtfs_route_date)")


def downgrade():
    op.execute("drop materialized view gtfs_rides_agg")
    op.execute("drop index idx_gtfs_rides_agg_gtfs_route_id")
    op.execute("drop index idx_gtfs_rides_agg_gtfs_route_date")
