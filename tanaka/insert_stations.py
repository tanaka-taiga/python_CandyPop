from datetime import date
from database import session
from makedb_stations import stations

stations= stations(
    seq = 6,
    name = "新大阪",
    kilo = "515.35"
)
session.add(stations)
session.commit()