from SimConnect import SimConnect, AircraftRequests
import time
from Class.database import SessionLocal
from CRUD import create_measurement, create_flight, update_flight
from datetime import datetime
from Calculations import get_wind_direction, get_wind_speed, get_pressure

def insert_measurement(db, flight_id):
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

    create_measurement(db, datetime.now(), latitude, longitude, altitude, altitude_agl, indicated_airspeed, ground_speed,
                       vertical_speed, pitch, roll, yaw, vario, g_force, wind_direction, wind_force, temperature,
                       pressure,
                       flight_id)

sm = SimConnect()
aq = AircraftRequests(sm)
db = SessionLocal()
no_sim = False

try:
    current_flight = create_flight(db, datetime.now(), f"{aq.get("PLANE_LATITUDE")},{aq.get("PLANE_LONGITUDE")}",
                                   f"", None, None)
except Exception as e:
    print("Impossible de créer un nouveau vol, le simulateur n'est pas en marche.")
    no_sim = True

while not no_sim:
    try:
        insert_measurement(db, current_flight.Id)

        if aq.get("AIRSPEED_INDICATED") < 3 and aq.get("GROUND_VELOCITY") < 3 and -15 < aq.get("VERTICAL_SPEED") < 3:
            update_flight(db, current_flight.Id, None, None, None, datetime.now(),
                        f"{aq.get("PLANE_LATITUDE")},{aq.get("PLANE_LONGITUDE")}")
            break

        time.sleep(10)
    except Exception as e:
        print("Impossible d'enregistrer les données du vol, le simulateur n'est plus en marche")
        no_sim = True

sm.exit()