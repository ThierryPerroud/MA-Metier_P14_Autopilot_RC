from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class gliders_has_flights(Base):
    __tablename__ = "gliders_has_flights"
    glider_id = Column(Integer, ForeignKey("gliders.Id"), primary_key=True)
    flight_id = Column(Integer, ForeignKey("flights.Id"), primary_key=True)

    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"