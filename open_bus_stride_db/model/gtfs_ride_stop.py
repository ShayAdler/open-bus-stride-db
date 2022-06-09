from .base import Base

import sqlalchemy.orm

from open_bus_stride_db.model.base import DateTimeWithTimeZone, info


class GtfsRideStop(Base):
    __tablename__ = 'gtfs_ride_stop'
    __table_args__ = (
        {**info("""
            A planned stop along a [[gtfs_ride]]. 
            Populated daily from the MOT GTFS data by [[gtfs-etl]]. 
        """)},
        sqlalchemy.Index(
            'idx_gtfs_ride_stop_arrival_time',
            sqlalchemy.text("date_trunc('day', arrival_time)::date")
        ),
    )

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_stop_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_stop.id'), index=True,
        **info("The related [[gtfs_stop]].")
    )
    gtfs_stop = sqlalchemy.orm.relationship(
        'GtfsStop', back_populates='gtfs_ride_stops',
        foreign_keys=[gtfs_stop_id]
    )
    gtfs_ride_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_ride.id'), index=True,
        **info("The related [[gtfs_ride]].")
    )
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
