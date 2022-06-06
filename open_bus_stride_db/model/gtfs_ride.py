import sqlalchemy.orm

from .base import Base, DateTimeWithTimeZone, info


class GtfsRide(Base):
    __tablename__ = 'gtfs_ride'
    __table_args__ = (
        {**info("""
            A planned ride (AKA trip) along a specified route. 
            Populated daily from the MOT GTFS data by [[gtfs-etl]]. 
        """)}
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    gtfs_route_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_route.id'), index=True,
        **info("The related [[gtfs_route]] this ride is a part of.")
    )
    gtfs_route = sqlalchemy.orm.relationship(
        'GtfsRoute', back_populates='gtfs_rides',
        foreign_keys=[gtfs_route_id]
    )
    journey_ref = sqlalchemy.Column(
        sqlalchemy.String, index=True,
        **info("A unique identifier for this ride as provided by the original MOT GTFS data.")
    )
    gtfs_ride_stops = sqlalchemy.orm.relationship(
        'GtfsRideStop', back_populates='gtfs_ride',
        primaryjoin="GtfsRide.id==GtfsRideStop.gtfs_ride_id"
    )
    first_gtfs_ride_stop_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_ride_stop.id'),
        **info("""
            The first [[gtfs_ride_stop]] along this ride. 
            Populated from [[stride-etl-gtfs-update-ride-aggregations]].
        """)
    )
    last_gtfs_ride_stop_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('gtfs_ride_stop.id'),
        **info("""
            The last [[gtfs_ride_stop]] along this ride. 
            Populated from [[stride-etl-gtfs-update-ride-aggregations]].
        """)
    )
    start_time = sqlalchemy.Column(
        DateTimeWithTimeZone,
        **info("""
            The start time of this ride. 
            Populated from [[stride-etl-gtfs-update-ride-aggregations]].
        """)
    )
    end_time = sqlalchemy.Column(
        DateTimeWithTimeZone,
        **info("""
            The end time of this ride. 
            Populated from [[stride-etl-gtfs-update-ride-aggregations]].
        """)
    )
