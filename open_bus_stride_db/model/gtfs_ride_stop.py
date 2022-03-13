from .base import Base

import sqlalchemy.orm

from open_bus_stride_db.model.base import DateTimeWithTimeZone


class GtfsRideStop(Base):
    __tablename__ = 'gtfs_ride_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_stop.id'), index=True)
    gtfs_stop = sqlalchemy.orm.relationship(
        'GtfsStop', back_populates='gtfs_ride_stops',
        foreign_keys=[gtfs_stop_id]
    )
    gtfs_ride_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_ride.id'), index=True)
    gtfs_ride = sqlalchemy.orm.relationship(
        'GtfsRide', back_populates='gtfs_ride_stops',
        foreign_keys=[gtfs_ride_id]
    )
    arrival_time = sqlalchemy.Column(DateTimeWithTimeZone)
    departure_time = sqlalchemy.Column(DateTimeWithTimeZone)
    stop_sequence = sqlalchemy.Column(sqlalchemy.Integer)
    pickup_type = sqlalchemy.Column(sqlalchemy.Integer)
    drop_off_type = sqlalchemy.Column(sqlalchemy.Integer)
    shape_dist_traveled = sqlalchemy.Column(sqlalchemy.Integer)
