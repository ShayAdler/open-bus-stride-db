from .base import Base, info

import sqlalchemy.orm


class SiriRoute(Base):
    __tablename__ = 'siri_route'
    __table_args__ = (
        sqlalchemy.Index(
            'idx_operator_ref_line_ref',
            'operator_ref', 'line_ref',
            unique=True
        ),
        {**info("""
            A SIRI route, populated in near real time from the SIRI data.
            Multiple rides can occur on a route, these are available in [[siri_ride]]
            and related by [[siri_ride.siri_route_id]].
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    line_ref = sqlalchemy.Column(
        sqlalchemy.Integer, index=True,
        **info("In combination with the [[operator_ref]] - uniquely identifies the route and relates to the GTFS identifiers")
    )
    operator_ref = sqlalchemy.Column(
        sqlalchemy.Integer, index=True,
        **info("In combination with the [[line_ref]] - uniquely identifies the route and relates to the GTFS identifiers")
    )
    siri_rides = sqlalchemy.orm.relationship(
        'SiriRide', back_populates='siri_route',
        primaryjoin='SiriRoute.id==SiriRide.siri_route_id'
    )
