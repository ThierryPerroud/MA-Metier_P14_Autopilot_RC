from sqlalchemy import Column, Integer, String, REAL
from database import Base

class Gliders(Base):
    __tablename__ = "gliders"

    Id = Column(Integer, primary_key=True)
    Model = Column(String)
    Empty_weight = Column(Integer)
    Center_gravity = Column(REAL)

    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"