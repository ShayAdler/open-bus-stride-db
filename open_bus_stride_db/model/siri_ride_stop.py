from .base import Base, info

import sqlalchemy.orm


class SiriRideStop(Base):
    __tablename__ = 'siri_ride_stop'
    __table_args__ = (
        sqlalchemy.Index(
            'idx_ride_stop_order',
            'siri_ride_id', 'siri_stop_id', 'order',
            unique=True
        ),
        {**info("""
            A stop along a ride received from the SIRI data.
            All SIRI Vehicle locations are related to this object on [[siri_vehicle_location.siri_ride_stop_id]] 
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    siri_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_stop.id'), index=True)
    siri_stop = sqlalchemy.orm.relationship(
        'SiriStop', back_populates='siri_ride_stops',
        foreign_keys=[siri_stop_id]
    )
    siri_ride_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_ride.id'), index=True)
    siri_ride = sqlalchemy.orm.relationship(
        'SiriRide', back_populates='siri_ride_stops',
        foreign_keys=[siri_ride_id]
    )
    order = sqlalchemy.Column(sqlalchemy.Integer, index=True, **info(
        "The order of this stop along the ride, first stop is 0"))
    siri_vehicle_locations = sqlalchemy.orm.relationship(
        'SiriVehicleLocation', back_populates='siri_ride_stop',
        primaryjoin='SiriRideStop.id==SiriVehicleLocation.siri_ride_stop_id'
    )
    gtfs_stop_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_stop.id'),
        **info("The related [[gtfs_stop]]"))
    nearest_siri_vehicle_location_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_vehicle_location.id'), index=True,
        **info(""))
