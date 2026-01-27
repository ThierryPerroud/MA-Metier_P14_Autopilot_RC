# Program name: Class.gliders_has_flight.py
# Description: Defines the gliders_has_flight class (unused, but kept for futureproofing)
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from sqlalchemy import Column, Integer, ForeignKey
from Class.database import Base

# **********************************************************************************************************************
#   Clases
# **********************************************************************************************************************
class gliders_has_flights(Base):
    __tablename__ = "gliders_has_flights"
    glider_id = Column(Integer, ForeignKey("gliders.Id"), primary_key=True)
    flight_id = Column(Integer, ForeignKey("flights.Id"), primary_key=True)

    def __repr__(self):
        return f"<glider_has_flights {self.glider_id} {self.flight_id}>"