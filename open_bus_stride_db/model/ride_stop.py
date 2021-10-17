from .base import Base

import sqlalchemy.orm


class RideStop(Base):
    __tablename__ = 'ride_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    route_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('route_stop.id'), index=True)
    route_stop = sqlalchemy.orm.relationship('RouteStop', back_populates='ride_stops')
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean, index=True)
    gtfs_arrival_datetime = sqlalchemy.Column(sqlalchemy.DateTime)
    gtfs_departure_datetime = sqlalchemy.Column(sqlalchemy.DateTime)
    gtfs_stop_sequence = sqlalchemy.Column(sqlalchemy.Integer)
    gtfs_pickup_type = sqlalchemy.Column(sqlalchemy.Integer)
    gtfs_drop_off_type = sqlalchemy.Column(sqlalchemy.Integer)
    gtfs_shape_dist_traveled = sqlalchemy.Column(sqlalchemy.Integer)
