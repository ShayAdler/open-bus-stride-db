import enum

from .base import Base

import sqlalchemy.orm


class SiriSnapshotEtlStatusEnum(enum.Enum):
    loading = 'loading'
    loaded = 'loaded'
    error = 'error'
    deleted = 'deleted'


class SiriSnapshot(Base):
    __tablename__ = 'siri_snapshot'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    snapshot_id = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    etl_status = sqlalchemy.Column(sqlalchemy.Enum(SiriSnapshotEtlStatusEnum))
    etl_start_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), index=True)
    etl_end_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
    error = sqlalchemy.Column(sqlalchemy.String)
    num_successful_parse_vehicle_locations = sqlalchemy.Column(sqlalchemy.Integer)
    num_failed_parse_vehicle_locations = sqlalchemy.Column(sqlalchemy.Integer)
    siri_vehicle_locations = sqlalchemy.orm.relationship('SiriVehicleLocation', back_populates='siri_snapshot')
    num_added_siri_rides = sqlalchemy.Column(sqlalchemy.Integer)
    num_added_siri_ride_stops = sqlalchemy.Column(sqlalchemy.Integer)
    num_added_siri_routes = sqlalchemy.Column(sqlalchemy.Integer)
    num_added_siri_stops = sqlalchemy.Column(sqlalchemy.Integer)
    last_heartbeat = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
    created_by = sqlalchemy.Column(sqlalchemy.String)
