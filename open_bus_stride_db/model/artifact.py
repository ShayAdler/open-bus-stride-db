import enum

import sqlalchemy.orm

from .base import Base, info, DateTimeWithTimeZone


class ArtifactStatusEnum(enum.Enum):
    uploading = 'uploading'
    error = 'error'
    success = 'success'


class Artifact(Base):
    __tablename__ = 'artifact'
    __table_args__ = (
        {**info("""
            Static files from ETL / processing tasks stored in S3. 
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    file_prefix = sqlalchemy.Column(sqlalchemy.String, index=True)
    status = sqlalchemy.Column(sqlalchemy.Enum(ArtifactStatusEnum), index=True)
    metadata_json = sqlalchemy.Column(sqlalchemy.String)
    error = sqlalchemy.Column(sqlalchemy.String)
    url = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(DateTimeWithTimeZone, index=True)
    file_size_bytes = sqlalchemy.Column(sqlalchemy.Integer)
