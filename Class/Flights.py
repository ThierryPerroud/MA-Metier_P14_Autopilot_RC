# Program name: Class.Flights.py
# Description: Defines the Flights class
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from sqlalchemy import Column, Integer, String
from Class.database import Base

# **********************************************************************************************************************
#   Clases
# **********************************************************************************************************************
class Flights(Base):
    __tablename__ = "flights"

    Id = Column(Integer, primary_key=True)
    Starting_date = Column(String)          # datetime.now() (at the beginning of the flight
    Starting_location = Column(String)      # PLANE_LATITUDE, PLANE_LONGITUDE (at the beginning of the flight)
    Destination_location = Column(String)   # TBD
    Ending_date = Column(String)            # datetime.now() (at the end of the flight)
    Ending_location = Column(String)        # PLANE_LATITUDE, PLANE_LONGITUDE (at the end of the flight)


    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"