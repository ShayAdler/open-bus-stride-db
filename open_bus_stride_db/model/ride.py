import sqlalchemy.orm

from .base import Base


class Ride(Base):
    __tablename__ = 'ride'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    route_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('route.id'), index=True)
    route = sqlalchemy.orm.relationship('Route', back_populates='rides')
    journey_ref = sqlalchemy.Column(sqlalchemy.String, index=True)
    scheduled_start_time = sqlalchemy.Column(sqlalchemy.DateTime, index=True)
    vehicle_ref = sqlalchemy.Column(sqlalchemy.String, index=True)
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean, index=True)
    # direction
    # planned_start_time
    # planned_end_time
    # planned_start_stop_id
    # planned_end_stop_id
    # num_vehicle_locations
    # siri_ride_id
    # is_passed_near_first_stop
    # is_passed_near_last_stop
    # percent_passed_planned_route_stops
    # is_valid_ride
    vehicle_locations = sqlalchemy.orm.relationship('VehicleLocation', back_populates='ride')
