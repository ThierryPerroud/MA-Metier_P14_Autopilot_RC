from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from Class.database import Base

class Telemetry_measurements(Base):
    __tablename__ = "telemetry_measurements"

    Id = Column(Integer, primary_key=True)
    Timestamp = Column(String)
    Latitude = Column(REAL)
    Longitude = Column(REAL)
    Altitude = Column(Integer)
    Altitude_agl = Column(Integer)
    Indicated_airspeed = Column(REAL)
    Ground_speed = Column(REAL)
    Pitch = Column(REAL)
    Roll = Column(REAL)
    Yaw = Column(REAL)
    Vario = Column(REAL)
    G_factor = Column(REAL)
    Wind_direction = Column(Integer)
    Wind_force = Column(REAL)
    Temperature = Column(REAL)
    Pression= Column(REAL)
    Flight_id = Column(Integer, ForeignKey("flights.Id"))

    def __repr__(self):
        return f"<glider {self.Id} {self.Model} {self.Empty_weight} {self.Center_gravity}>"