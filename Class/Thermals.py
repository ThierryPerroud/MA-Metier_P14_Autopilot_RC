from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from Class.database import Base

class Thermals(Base):
    __tablename__ = "thermals"

    Id = Column(Integer, primary_key=True)
    Min_atltitude = Column(Integer)
    Max_altitude = Column(Integer)
    Avg_variometer = Column(REAL)
    Start = Column(String)
    End = Column(String)
    Flight_id = Column(Integer, ForeignKey("flights.Id"))

    def __repr__(self):
        return f"<thermals {self.Id} {self.Min_atltitude} {self.Max_altitude} {self.Avg_variometer} {self.Start} {self.End} {self.Flight_id}>"