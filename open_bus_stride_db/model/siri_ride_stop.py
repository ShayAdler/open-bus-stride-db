from .base import Base

import sqlalchemy.orm


class SiriRideStop(Base):
    __tablename__ = 'siri_ride_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    siri_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_stop.id'), index=True)
    siri_stop = sqlalchemy.orm.relationship('SiriStop', back_populates='siri_ride_stops')
    siri_ride_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_ride.id'), index=True)
    siri_ride = sqlalchemy.orm.relationship('SiriRide', back_populates='siri_ride_stops')
    order = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    siri_vehicle_locations = sqlalchemy.orm.relationship('SiriVehicleLocation', back_populates='siri_ride_stop')
