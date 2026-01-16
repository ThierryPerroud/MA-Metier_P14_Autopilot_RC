from sqlalchemy import Column, Integer, String
from database import Base

class Flights(Base):
    __tablename__ = "flights"

    Id = Column(Integer, primary_key=True)
    Starting_date = Column(String)
    Ending_date = Column(String)


    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"