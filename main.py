from SimConnect import SimConnect, AircraftRequests
import time
from Class.database import SessionLocal
from CRUD import *
from datetime import datetime
from Calculations import *

def insert_measurement():
    db = SessionLocal()
    timestamp = datetime.now()
    latitude = aq.get("PLANE_LATITUDE")
    longitude = aq.get("PLANE_LONGITUDE")
    altitude = aq.get("PLANE_ALTITUDE")
    altitude_agl = aq.get("PLANE_ALT_ABOVE_GROUND")
    indicated_airspeed = aq.get("AIRSPEED_INDICATED")
    ground_speed = aq.get("GROUND_VELOCITY")
    vertical_speed = aq.get("VERTICAL_SPEED")
    pitch = aq.get("PLANE_PITCH_DEGREES")
    roll = aq.get("PLANE_BANK_DEGREES")
    yaw = aq.get("PLANE_HEADING_DEGREES_MAGNETIC")
    vario = aq.get("VARIOMETER_RATE")
    g_force = aq.get("G_FORCE")
    wind_direction = get_wind_direction(aq.get("AIRCRAFT_WIND_X"), aq.get("AIRCRAFT_WIND_Z"),
                                        aq.get("PLANE_HEADING_DEGREES_MAGNETIC"))
    wind_force = get_wind_speed(aq.get("AIRCRAFT_WIND_X"), aq.get("AIRCRAFT_WIND_Y"), aq.get("AIRCRAFT_WIND_Z"))
    temperature = aq.get("TOTAL_AIR_TEMPERATURE")
    pressure = get_pressure(aq.get("SEA_LEVEL_PRESSURE"), aq.get("PLANE_ALTITUDE"))
    flight_id = None

    create_measurement(db, timestamp, latitude, longitude, altitude, altitude_agl, indicated_airspeed, ground_speed,
                       vertical_speed, pitch, roll, yaw, vario, g_force, wind_direction, wind_force, temperature,
                       pressure,
                       flight_id)



while True:
    sm = SimConnect()
    aq = AircraftRequests(sm)

    time.sleep(10)
    insert_measurement()

    sm.exit()