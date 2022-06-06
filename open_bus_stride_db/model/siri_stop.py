from .base import Base, info

import sqlalchemy.orm


class SiriStop(Base):
    __tablename__ = 'siri_stop'
    __table_args__ = (
        {**info("""
            A SIRI stop, populated in near real time from the SIRI data by [[siri-etl-process-snapshot-new-snapshots-daemon]].
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    code = sqlalchemy.Column(
        sqlalchemy.Integer, index=True, unique=True,
        **info("Corresponds to the GTFS stop code, as received from the SIRI data.")
    )
    siri_ride_stops = sqlalchemy.orm.relationship(
        'SiriRideStop', back_populates='siri_stop',
        primaryjoin='SiriStop.id==SiriRideStop.siri_stop_id'
    )
