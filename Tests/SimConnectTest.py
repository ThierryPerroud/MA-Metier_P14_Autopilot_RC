from SimConnect import SimConnect, AircraftRequests
from Class.database import SessionLocal
from CRUD import *
from datetime import datetime

sm = SimConnect()
aq = AircraftRequests(sm)
db = SessionLocal()

mesure = create_measurement(
    db=db,
    timestamp=datetime.now(),
    latitude=None,
    longitude=None,
    altitude=None,
    altitude_agl=None,
    indicated_airspeed=None,
    ground_speed=None,
    pitch=None,
    roll=None,
    yaw=None,
    vario=None,
    g_force=None,
    wind_direction=None,
    wind_force=None,
    temperature=None,
    pressure=None,
    flight_id=None
)