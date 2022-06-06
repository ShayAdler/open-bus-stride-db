from .base import Base, info

import sqlalchemy.orm


class GtfsStop(Base):
    __tablename__ = 'gtfs_stop'
    __table_args__ = (
        {**info("""
            A single stop. 
            Populated daily from the MOT GTFS data by [[gtfs-etl]]. 
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(
        sqlalchemy.Date, index=True,
        **info("""
            Because the GTFS data may change daily, each stop is relevant only for a single day specified in this field.
        """)
    )
    code = sqlalchemy.Column(
        sqlalchemy.Integer, index=True,
        **info("The GTFS stop code.")
    )
    lat = sqlalchemy.Column(sqlalchemy.Float)
    lon = sqlalchemy.Column(sqlalchemy.Float)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    gtfs_ride_stops = sqlalchemy.orm.relationship(
        'GtfsRideStop', back_populates='gtfs_stop',
        primaryjoin='GtfsStop.id==GtfsRideStop.gtfs_stop_id'
    )
    gtfs_stop_mot_ids = sqlalchemy.orm.relationship(
        'GtfsStopMotId', back_populates='gtfs_stop',
        primaryjoin='GtfsStop.id==GtfsStopMotId.gtfs_stop_id'
    )
