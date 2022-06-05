import enum

from .base import Base, DateTimeWithTimeZone, info

import sqlalchemy.orm


class SiriSnapshotEtlStatusEnum(enum.Enum):
    loading = 'loading'
    loaded = 'loaded'
    error = 'error'
    deleted = 'deleted'


class SiriSnapshot(Base):
    __tablename__ = 'siri_snapshot'
    __table_args__ = (
        {**info("""
            A SIRI Snapshot which was received from MOT. We get a new snapshot every 1 minute.
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    snapshot_id = sqlalchemy.Column(
        sqlalchemy.String, index=True, unique=True,
        **info("""
            A string which uniquely identifies the snapshot and the date/time when it was taken.
            Uses the following format: year/month/day/hours/minutes (e.g. 2022/03/09/11/08).
        """)
    )
    etl_status = sqlalchemy.Column(
        sqlalchemy.Enum(SiriSnapshotEtlStatusEnum),
        **info("""
            Describes the ETL status of this snapshot, 
            only snapshots with status "loaded" should be considered ready for usage. 
        """)
    )
    etl_start_time = sqlalchemy.Column(DateTimeWithTimeZone, index=True)
    etl_end_time = sqlalchemy.Column(DateTimeWithTimeZone)
    error = sqlalchemy.Column(
        sqlalchemy.String,
        **info("""
            If the ETL processing failed for this snapshot, will contain the error message.
        """)
    )
    num_successful_parse_vehicle_locations = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Number of [[siri_vehicle_location]]s which were successfully parsed from this SIRI snapshot.
        """)
    )
    num_failed_parse_vehicle_locations = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Number of [[siri_vehicle_location]]s which failed to be parsed from this SIRI snapshot.
        """)
    )
    siri_vehicle_locations = sqlalchemy.orm.relationship(
        'SiriVehicleLocation', back_populates='siri_snapshot',
        primaryjoin='SiriSnapshot.id==SiriVehicleLocation.siri_snapshot_id'
    )
    num_added_siri_rides = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Number of new [[siri_ride]]s which were added as a result of processing this SIRI snapshot.
        """)
    )
    num_added_siri_ride_stops = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Number of new [[siri_ride_stop]]s which were added as a result of processing this SIRI snapshot.
        """)
    )
    num_added_siri_routes = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Number of new [[siri_route]]s which were added as a result of processing this SIRI snapshot.
        """)
    )
    num_added_siri_stops = sqlalchemy.Column(
        sqlalchemy.Integer,
        **info("""
            Number of new [[siri_stop]]s which were added as a result of processing this SIRI snapshot.
        """)
    )
    last_heartbeat = sqlalchemy.Column(DateTimeWithTimeZone, **info(hide=True))
    created_by = sqlalchemy.Column(sqlalchemy.String, **info(hide=True))
