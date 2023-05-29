from datetime import date
from database import session
from table_station import Station
import sys
args = sys.argv
input1 = str(args[1])
input2 = str(args[2])

station1 = session.query(Station.kilo).filter_by(name = input1).first()
station2 = session.query(Station.kilo).filter_by(name = input2).first()

if(station1 >= station2):
    result  = station1[0] - station2[0]
else:
    result = station2[0] - station1[0]

print(result)
