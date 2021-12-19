from .base import Base

import sqlalchemy.orm


class GtfsRoute(Base):
    __tablename__ = 'gtfs_route'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    line_ref = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    operator_ref = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    route_short_name = sqlalchemy.Column(sqlalchemy.String)
    route_long_name = sqlalchemy.Column(sqlalchemy.String)
    route_mkt = sqlalchemy.Column(sqlalchemy.String)
    route_direction = sqlalchemy.Column(sqlalchemy.String)
    route_alternative = sqlalchemy.Column(sqlalchemy.String)
    agency_name = sqlalchemy.Column(sqlalchemy.String)
    route_type = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_stops = sqlalchemy.orm.relationship('GtfsRouteStop', back_populates='gtfs_route')
    gtfs_rides = sqlalchemy.orm.relationship('GtfsRide', back_populates='gtfs_route')
