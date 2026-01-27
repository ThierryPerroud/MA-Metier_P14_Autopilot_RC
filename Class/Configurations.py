# Program name: Class.Configuration.py
# Description: Defines the Configuration class (unused, but is kept for futureproofing)
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from sqlalchemy import Column, Integer, REAL, ForeignKey
from Class.database import Base

# **********************************************************************************************************************
#   Clases
# **********************************************************************************************************************
class Configurations(Base):
    __tablename__ = "configurations"

    Id = Column(Integer, primary_key=True)
    Ballast_water = Column(REAL)        # TBD
    Airbrake_position = Column(Integer) # TBD
    Flaps = Column(Integer)             # TBD
    glider_id = Column(Integer, ForeignKey('gliders.Id'))

    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"