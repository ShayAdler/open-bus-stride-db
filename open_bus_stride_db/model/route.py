from .base import Base

import sqlalchemy


class Route(Base):
    __tablename__ = 'route'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    min_date = sqlalchemy.Column(sqlalchemy.Date)
    max_date = sqlalchemy.Column(sqlalchemy.Date)
    line_ref = sqlalchemy.Column(sqlalchemy.Integer)
    operator_ref = sqlalchemy.Column(sqlalchemy.Integer)
    siri_published_line_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_short_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_long_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_mkt = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_direction = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_alternative = sqlalchemy.Column(sqlalchemy.String)
    gtfs_agency_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_type = sqlalchemy.Column(sqlalchemy.String)
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean)
