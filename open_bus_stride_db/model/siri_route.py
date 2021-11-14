from .base import Base

import sqlalchemy.orm


class SiriRoute(Base):
    __tablename__ = 'siri_route'
    __table_args__ = (
        sqlalchemy.Index(
            'idx_operator_ref_line_ref',
            'operator_ref', 'line_ref',
            unique=True
        ),
    )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    line_ref = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    operator_ref = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    siri_rides = sqlalchemy.orm.relationship('SiriRide', back_populates='siri_route')
