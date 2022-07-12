import sqlalchemy.orm

from .base import Base, info, DateTimeWithTimeZone


class GtfsDataTask(Base):
    __tablename__ = 'gtfs_data_task'
    __table_args__ = (
        sqlalchemy.Index(
            'idx_gtfs_data_task_id_name',
            'gtfs_data_id', 'task_name',
            unique=True
        ),
        {**info("""
            Record of processing tasks status relating to GTFS data. 
        """)},
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_data_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_data.id'))
    task_name = sqlalchemy.Column(sqlalchemy.String, index=True)
    started_at = sqlalchemy.Column(DateTimeWithTimeZone)
    completed_at = sqlalchemy.Column(DateTimeWithTimeZone)
    error = sqlalchemy.Column(sqlalchemy.String)
    success = sqlalchemy.Column(sqlalchemy.Boolean)
