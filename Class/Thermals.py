# Program name: Class.Thermals.py
# Description: Defines the Thermals class (unused but kept for futureproofing)
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from Class.database import Base

# **********************************************************************************************************************
#   Clases
# **********************************************************************************************************************
class Thermals(Base):
    __tablename__ = "thermals"

    Id = Column(Integer, primary_key=True)
    Min_atltitude = Column(Integer) # TBD
    Max_altitude = Column(Integer)  # TBD
    Avg_variometer = Column(REAL)   # TBD
    Start = Column(String)          # TBD
    End = Column(String)            # TBD
    Flight_id = Column(Integer, ForeignKey("flights.Id"))

    def __repr__(self):
        return f"<thermals {self.Id} {self.Min_atltitude} {self.Max_altitude} {self.Avg_variometer} {self.Start} {self.End} {self.Flight_id}>"