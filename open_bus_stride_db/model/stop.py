from .base import Base

import sqlalchemy.orm


class Stop(Base):
    __tablename__ = 'stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    min_date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    max_date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    code = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    lon = sqlalchemy.Column(sqlalchemy.Float)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean, index=True)
    route_stops = sqlalchemy.orm.relationship('RouteStop', back_populates='stop')
