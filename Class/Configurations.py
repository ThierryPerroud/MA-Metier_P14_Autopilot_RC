from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from database import Base

class Configurations(Base):
    __tablename__ = "configurations"

    Id = Column(Integer, primary_key=True)
    Ballast_water = Column(REAL)
    Airbrake_position = Column(Integer)
    Flaps = Column(Integer)
    glider_id = Column(Integer, ForeignKey('gliders.Id'))

    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"