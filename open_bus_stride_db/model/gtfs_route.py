from .base import Base, info

import sqlalchemy.orm


class GtfsRoute(Base):
    __tablename__ = 'gtfs_route'
    __table_args__ = (
        {**info("""
            A planned route. 
            Populated daily from the MOT GTFS data by [[gtfs-etl]]. 
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(
        sqlalchemy.Date, index=True,
        **info("""
            Because the GTFS data may change daily, each route is only relevant for a single day specified in this field.
        """)
    )
    line_ref = sqlalchemy.Column(
        sqlalchemy.Integer, index=True,
        **info("Unique identifier for this route, together with [[operator_ref]].")
    )
    operator_ref = sqlalchemy.Column(
        sqlalchemy.Integer, index=True,
        **info("Unique identifier for this route, together with [[line_ref]].")
    )
    route_short_name = sqlalchemy.Column(sqlalchemy.String)
    route_long_name = sqlalchemy.Column(sqlalchemy.String)
    route_mkt = sqlalchemy.Column(sqlalchemy.String)
    route_direction = sqlalchemy.Column(sqlalchemy.String)
    route_alternative = sqlalchemy.Column(sqlalchemy.String)
    agency_name = sqlalchemy.Column(sqlalchemy.String)
    route_type = sqlalchemy.Column(sqlalchemy.String)
    gtfs_rides = sqlalchemy.orm.relationship(
        'GtfsRide', back_populates='gtfs_route', cascade="all, delete",
        primaryjoin='GtfsRoute.id==GtfsRide.gtfs_route_id'
    )
