from .base import Base

import sqlalchemy.orm


class GtfsStopMotId(Base):
    __tablename__ = 'gtfs_stop_mot_id'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_stop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_stop.id'), index=True)
    gtfs_stop = sqlalchemy.orm.relationship(
        'GtfsStop', back_populates='gtfs_stop_mot_ids',
        foreign_keys=[gtfs_stop_id]
    )
    mot_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
