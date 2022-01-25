from .base import Base, DateTimeWithTimeZone

import sqlalchemy.orm


class SiriVehicleLocation(Base):
    __tablename__ = 'siri_vehicle_location'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    siri_snapshot_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_snapshot.id'), index=True)
    siri_snapshot = sqlalchemy.orm.relationship('SiriSnapshot', back_populates='siri_vehicle_locations')
    siri_ride_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_ride_stop.id'), index=True)
    siri_ride_stop = sqlalchemy.orm.relationship('SiriRideStop', back_populates='siri_vehicle_locations')
    recorded_at_time = sqlalchemy.Column(DateTimeWithTimeZone, index=True)
    lon = sqlalchemy.Column(sqlalchemy.Float)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    bearing = sqlalchemy.Column(sqlalchemy.Integer)
    velocity = sqlalchemy.Column(sqlalchemy.Integer)
    distance_from_journey_start = sqlalchemy.Column(sqlalchemy.Integer)
    distance_from_siri_ride_stop_meters = sqlalchemy.Column(sqlalchemy.Integer)
