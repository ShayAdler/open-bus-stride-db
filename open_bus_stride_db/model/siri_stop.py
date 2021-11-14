from .base import Base

import sqlalchemy.orm


class SiriStop(Base):
    __tablename__ = 'siri_stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    code = sqlalchemy.Column(sqlalchemy.Integer, index=True, unique=True)
    siri_ride_stops = sqlalchemy.orm.relationship('SiriRideStop', back_populates='siri_stop')
