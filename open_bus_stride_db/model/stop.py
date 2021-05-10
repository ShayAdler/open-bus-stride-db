from .base import Base

import sqlalchemy.orm


class Stop(Base):
    __tablename__ = 'stop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    min_date = sqlalchemy.Column(sqlalchemy.Date)
    max_date = sqlalchemy.Column(sqlalchemy.Date)
    code = sqlalchemy.Column(sqlalchemy.Integer)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    lon = sqlalchemy.Column(sqlalchemy.Float)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean)
    route_stops = sqlalchemy.orm.relationship('RouteStop', back_populates='stop')
