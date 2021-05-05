import datetime

from sqlalchemy.orm import Session

from open_bus_stride_db.model import Route


def test_route(session: Session):
    session.query(Route).delete()
    siri_route = Route(
        min_date=datetime.date(2020, 5, 4),
        max_date=datetime.date(2021, 5, 4),
        line_ref=5,
        operator_ref=123,
        siri_published_line_name='קו 5 בדרך אל הים',
    )
    gtfs_route = Route(
        min_date=datetime.date(2021, 2, 4),
        max_date=datetime.date(2021, 3, 4),
        line_ref=5,
        operator_ref=123,
        gtfs_route_short_name='קו 5',
        gtfs_route_long_name='קו 5 בדרך אל הים',
        is_from_gtfs=True
    )
    session.add_all([siri_route, gtfs_route])
    assert session.query(Route).count() == 2
