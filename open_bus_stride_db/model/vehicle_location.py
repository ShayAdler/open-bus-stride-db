from .base import Base

import sqlalchemy.orm


class VehicleLocation(Base):
    __tablename__ = 'vehicle_location'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    siri_snapshot_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_snapshot.id'))
    siri_snapshot = sqlalchemy.orm.relationship('SiriSnapshot', back_populates='vehicle_locations')
    ride_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('ride.id'))
    ride = sqlalchemy.orm.relationship('Ride', back_populates='vehicle_locations')
    route_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('route_stop.id'))
    route_stop = sqlalchemy.orm.relationship('RouteStop', back_populates='vehicle_locations')
    recorded_at_time = sqlalchemy.Column(sqlalchemy.DateTime)
    lon = sqlalchemy.Column(sqlalchemy.Float)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    bearing = sqlalchemy.Column(sqlalchemy.Integer)
    velocity = sqlalchemy.Column(sqlalchemy.Integer)
    distance_from_journey_start = sqlalchemy.Column(sqlalchemy.Integer)
