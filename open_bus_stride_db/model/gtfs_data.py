import sqlalchemy.orm

from .base import Base, info, DateTimeWithTimeZone


class GtfsData(Base):
    __tablename__ = 'gtfs_data'
    __table_args__ = (
        {**info("""
            Record of downloaded GTFS data from MOT per day.
            Task and processing status relating to this day's GTFS data. 
        """)},
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    processing_started_at = sqlalchemy.Column(DateTimeWithTimeZone, index=True)
    processing_completed_at = sqlalchemy.Column(DateTimeWithTimeZone)
    processing_error = sqlalchemy.Column(sqlalchemy.String)
    processing_success = sqlalchemy.Column(sqlalchemy.Boolean)
    upload_success = sqlalchemy.Column(sqlalchemy.Boolean)
    processing_used_stride_date = sqlalchemy.Column(sqlalchemy.Date, **info("""
        If the GTFS data was processed using a different date then in the date field, this is the date used. 
    """))
