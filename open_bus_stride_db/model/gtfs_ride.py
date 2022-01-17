import sqlalchemy.orm

from .base import Base, DateTimeWithTimeZone


class GtfsRide(Base):
    __tablename__ = 'gtfs_ride'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_route_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_route.id'), index=True)
    gtfs_route = sqlalchemy.orm.relationship('GtfsRoute', back_populates='gtfs_rides')
    journey_ref = sqlalchemy.Column(sqlalchemy.String, index=True)
    gtfs_ride_stops = sqlalchemy.orm.relationship('GtfsRideStop', back_populates='gtfs_ride')

    # populated from open_bus_stride_etl.gtfs.update_ride_aggregations
    first_gtfs_ride_stop_id = sqlalchemy.Column(sqlalchemy.Integer)
    last_gtfs_ride_stop_id = sqlalchemy.Column(sqlalchemy.Integer)
    start_time = sqlalchemy.Column(DateTimeWithTimeZone)
    end_time = sqlalchemy.Column(DateTimeWithTimeZone)
