# Program name: Class.Gliders.py
# Description: Defines the Gliders class (unused, but kept for futureproofing)
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from sqlalchemy import Column, Integer, String, REAL
from Class.database import Base

# **********************************************************************************************************************
#   Clases
# **********************************************************************************************************************
class Gliders(Base):
    __tablename__ = "gliders"

    Id = Column(Integer, primary_key=True)
    Model = Column(String)          # TBD
    Empty_weight = Column(Integer)  # TBD
    Center_gravity = Column(REAL)   # TBD

    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"