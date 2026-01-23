from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from Class.database import Base

class Telemetry_measurements(Base):
    __tablename__ = "telemetry_measurements"

    Id = Column(Integer, primary_key=True)
    Timestamp = Column(String)          # datetime.now()
    Latitude = Column(REAL)             # PLANE_LATITUDE
    Longitude = Column(REAL)            # PLANE_LONGITUDE
    Altitude = Column(Integer)          # PLANE_ALTITUDE
    Altitude_agl = Column(Integer)      # PLANE_ALT_ABOVE_GROUND
    Indicated_airspeed = Column(REAL)   # AIRSPEED_INDICATED
    Ground_speed = Column(REAL)         # GROUND_VELOCITY
    Vertical_speed = Column(REAL)       # VERTICAL_SPEED
    Pitch = Column(REAL)                # PLANE_PITCH_DEGREES
    Roll = Column(REAL)                 # PLANE_BANK_DEGREES
    Yaw = Column(REAL)                  # PLANE_HEADING_DEGREES_MAGNETIC
    Vario = Column(REAL)                # VARIOMETER_RATE
    G_force = Column(REAL)              # G_FORCE
    Wind_direction = Column(Integer)    # get_wind_direction(AIRCRAFT_WIND_X, AIRCRAFT_WIND_Z, PLANE_HEADING_DEGREES_MAGNETIC)
    Wind_force = Column(REAL)           # get_wind_speed(AIRCRAFT_WIND_X + AIRCRAFT_WIND_Y + AIRCRAFT_WIND_Z)
    Temperature = Column(REAL)          # TOTAL_AIR_TEMPERATURE
    Pressure= Column(REAL)              # TBD
    Flight_id = Column(Integer, ForeignKey("flights.Id"))

    def __repr__(self):
        return (f"<telemetry measurements {self.Id} {self.Timestamp} {self.Latitude} {self.Longitude} {self.Altitude} {self.Altitude_agl} "
                f"{self.Indicated_airspeed} {self.Ground_speed} {self.Vertical_speed} {self.Pitch} {self.Roll} {self.Yaw} {self.Vario} {self.G_force} {self.Wind_direction} "
                f"{self.Wind_force} {self.Temperature} {self.Pressure} {self.Flight_id}>")