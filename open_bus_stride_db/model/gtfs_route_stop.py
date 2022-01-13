from .base import Base

import sqlalchemy.orm


class GtfsRouteStop(Base):
    __tablename__ = 'gtfs_route_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_stop.id'), index=True)
    gtfs_stop = sqlalchemy.orm.relationship('GtfsStop', back_populates='gtfs_route_stops', cascade="all, delete")
    gtfs_route_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_route.id'), index=True)
    gtfs_route = sqlalchemy.orm.relationship('GtfsRoute', back_populates='gtfs_route_stops')
    order = sqlalchemy.Column(sqlalchemy.Integer, index=True)
