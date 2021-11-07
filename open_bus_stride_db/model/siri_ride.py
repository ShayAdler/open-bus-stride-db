import sqlalchemy.orm

from .base import Base


class SiriRide(Base):
    __tablename__ = 'siri_ride'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    siri_route_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_route.id'), index=True)
    siri_route = sqlalchemy.orm.relationship('SiriRoute', back_populates='siri_rides')
    journey_ref = sqlalchemy.Column(sqlalchemy.String, index=True)
    scheduled_start_time = sqlalchemy.Column(sqlalchemy.DateTime, index=True)
    vehicle_ref = sqlalchemy.Column(sqlalchemy.String, index=True)
    siri_ride_stops = sqlalchemy.orm.relationship('SiriRideStop', back_populates='siri_ride')
