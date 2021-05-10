from .base import Base

import sqlalchemy.orm


class RouteStop(Base):
    __tablename__ = 'route_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('stop.id'))
    stop = sqlalchemy.orm.relationship('Stop', back_populates='route_stops')
    route_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('route.id'))
    route = sqlalchemy.orm.relationship('Route', back_populates='route_stops')
    order = sqlalchemy.Column(sqlalchemy.Integer)
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean)
    vehicle_locations = sqlalchemy.orm.relationship('VehicleLocation', back_populates='route_stop')
