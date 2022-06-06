from .base import Base, DateTimeWithTimeZone, info

import sqlalchemy.orm


class SiriVehicleLocation(Base):
    __tablename__ = 'siri_vehicle_location'
    __table_args__ = (
        {**info("""
            A vehicle location, accurate to within 1 minute, populated in near real time from the SIRI data.
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    siri_snapshot_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_snapshot.id'), index=True,
        **info("The [[siri_snapshot]] which contained this vehicle location.")
    )
    siri_snapshot = sqlalchemy.orm.relationship(
        'SiriSnapshot', back_populates='siri_vehicle_locations',
        foreign_keys=[siri_snapshot_id]
    )
    siri_ride_stop_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('siri_ride_stop.id'), index=True,
        **info("""
            The [[siri_ride_stop]] which is nearest to this vehicle location.
            This relation can be used to get all relevant details like route / ride / stop relating to this location.
        """)
    )
    siri_ride_stop = sqlalchemy.orm.relationship(
        'SiriRideStop', back_populates='siri_vehicle_locations',
        foreign_keys=[siri_ride_stop_id]
    )
    recorded_at_time = sqlalchemy.Column(
        DateTimeWithTimeZone, index=True,
        **info("The date/time when this location was recorded according to the MOT SIRI data.")
    )
    lon = sqlalchemy.Column(
        sqlalchemy.Float, index=True,
        **info("The geographical lon of this vehicle at the recorded time, according to the MOT SIRI data.")
    )
    lat = sqlalchemy.Column(
        sqlalchemy.Float, index=True,
        **info("The geographical lat of this vehicle at the recorded time, according to the MOT SIRI data.")
    )
    bearing = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("The bearing of this vehicle at the recorded time, according to the MOT SIRI data.")
    )
    velocity = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("The velocity of this vehicle at the recorded time, according to the MOT SIRI data.")
    )
    distance_from_journey_start = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("The distance from journey start of this vehicle at the recorded time, according to the MOT SIRI data.")
    )
    distance_from_siri_ride_stop_meters = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Distance from the nearest [[siri_ride_stop]] according to the GTFS stop location.
            Populated via [[stride-etl-siri-update-ride-stops-vehicle-locations]].
        """)
    )
