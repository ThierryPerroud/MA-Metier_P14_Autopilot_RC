from sqlalchemy import Column, Integer, ForeignKey
from Class.database import Base

class gliders_has_flights(Base):
    __tablename__ = "gliders_has_flights"
    glider_id = Column(Integer, ForeignKey("gliders.Id"), primary_key=True)
    flight_id = Column(Integer, ForeignKey("flights.Id"), primary_key=True)

    def __repr__(self):
        return f"<glider_has_flights {self.glider_id} {self.flight_id}>"