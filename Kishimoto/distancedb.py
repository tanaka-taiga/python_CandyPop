import sys
from sqlalchemy import Column, Integer,DECIMAL,String,Integer
from database import Base
from database import ENGINE

class Stations(Base):
    __tablename__ = 'stations'
    stations_seq  = Column('stations_seq',Integer,primary_key = True)
    stations_name = Column('stations_name',String(20))
    stations_kilo = Column('stations_kilo', DECIMAL(6,2))

def main(args):

    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
