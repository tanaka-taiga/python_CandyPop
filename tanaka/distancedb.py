import sys
from database import session
from makedb_stations import stations
args = sys.argv

station1 = args[1]
station2 = args[2]

stations_list = session.query(stations).all()

for i in stations_list:
    if i.name == station1:
        station1_kilo = i.kilo
    if i.name == station2:
        station2_kilo = i.kilo

kyori = station2_kilo - station1_kilo

print(kyori)
