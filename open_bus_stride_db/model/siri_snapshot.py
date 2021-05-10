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
    snapshot_id = sqlalchemy.Column(sqlalchemy.String)
    etl_status = sqlalchemy.Column(sqlalchemy.Enum(SiriSnapshotEtlStatusEnum))
    etl_start_time = sqlalchemy.Column(sqlalchemy.DateTime)
    etl_end_time = sqlalchemy.Column(sqlalchemy.DateTime)
    error = sqlalchemy.Column(sqlalchemy.String)
    num_successful_parse_vehicle_locations = sqlalchemy.Column(sqlalchemy.Integer)
    num_failed_parse_vehicle_locations = sqlalchemy.Column(sqlalchemy.Integer)
    vehicle_locations = sqlalchemy.orm.relationship('VehicleLocation', back_populates='siri_snapshot')
