import datetime

from sqlalchemy.orm import Session

from open_bus_stride_db.model import Stop


def test_route(session: Session):
    session.query(Stop).delete()
    siri_stop = Stop(
        min_date=datetime.date(2020, 5, 4),
        max_date=datetime.date(2021, 5, 4),
        code=323
    )
    gtfs_stop = Stop(
        min_date=datetime.date(2021, 2, 4),
        max_date=datetime.date(2021, 3, 4),
        code=333,
        lat=34.5543434,
        lon=33.493833,
        name='תחנה בסוף היקום',
        city='נוה חמציצים',
        is_from_gtfs=True
    )
    session.add_all([siri_stop, gtfs_stop])
    assert session.query(Stop).count() == 2
