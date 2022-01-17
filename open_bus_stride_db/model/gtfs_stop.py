from .base import Base

import sqlalchemy.orm


class GtfsStop(Base):
    __tablename__ = 'gtfs_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    code = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    lon = sqlalchemy.Column(sqlalchemy.Float)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    gtfs_ride_stops = sqlalchemy.orm.relationship('GtfsRideStop', back_populates='gtfs_stop')
    gtfs_stop_mot_ids = sqlalchemy.orm.relationship('GtfsStopMotId', back_populates='gtfs_stop')
