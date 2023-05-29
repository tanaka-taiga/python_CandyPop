from datetime import date
from database import session 
from tables import Stations

Station = Stations(
    stations_seq  = 1,
    stations_name = "東京",
    stations_kilo = 0.00
)

session.add(Station)
session.commit()