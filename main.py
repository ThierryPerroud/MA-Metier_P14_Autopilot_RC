# Program name: main.py
# Description: Main program of the glider autopilot
# Created by: Thierry Perroud
# Last modified by: Thierry Perroud
# Last Modified date: 28.01.2026
# Version : 0.6

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from SimConnect import SimConnect, AircraftRequests
from datetime import datetime
import math
import time
from Class import *
from CRUD import *
from Calculations import *
from ExportData import get_data

# **********************************************************************************************************************
#   Functions
# **********************************************************************************************************************

def insert_measurement(db, flight_id):
    '''
    Insert a measurement into the database
    '''
    latitude = aq.get("PLANE_LATITUDE")                                                         # degrees
    longitude = aq.get("PLANE_LONGITUDE")                                                       # degrees
    altitude = aq.get("PLANE_ALTITUDE")                                                         # feet
    altitude_agl = aq.get("PLANE_ALT_ABOVE_GROUND")                                             # feet
    ground_level = altitude - altitude_agl                                                      # feet
    indicated_airspeed = aq.get("AIRSPEED_INDICATED")                                           # knots/s
    ground_speed = aq.get("GROUND_VELOCITY")                                                    # knots/s
    vertical_speed = aq.get("VERTICAL_SPEED")                                                   # TBD
    pitch = math.degrees(aq.get("PLANE_PITCH_DEGREES"))                                         # degrees
    roll = math.degrees(aq.get("PLANE_BANK_DEGREES"))                                           # degrees
    yaw = math.degrees(aq.get("PLANE_HEADING_DEGREES_MAGNETIC"))                                # degrees
    vario = aq.get("VARIOMETER_RATE")                                                           # TBD
    g_force = aq.get("G_FORCE")                                                                 # TBD
    wind_direction = get_wind_direction(aq.get("AIRCRAFT_WIND_X"), aq.get("AIRCRAFT_WIND_Z"),   # degrees
                                        aq.get("PLANE_HEADING_DEGREES_MAGNETIC"))
    wind_force = get_wind_speed(aq.get("AIRCRAFT_WIND_X"), aq.get("AIRCRAFT_WIND_Y"),           # m/s
                                aq.get("AIRCRAFT_WIND_Z"))
    temperature = aq.get("TOTAL_AIR_TEMPERATURE")                                               # degrees Celsius
    pressure = get_pressure(aq.get("SEA_LEVEL_PRESSURE"), aq.get("PLANE_ALTITUDE"))             # atmosphere

    # Logs into the database all telemetry measurements
    create_measurement(db, datetime.now(), latitude, longitude, altitude, altitude_agl, ground_level, indicated_airspeed, ground_speed,
                       vertical_speed, pitch, roll, yaw, vario, g_force, wind_direction, wind_force, temperature,
                       pressure, flight_id)


# **********************************************************************************************************************
#   Variables
# **********************************************************************************************************************
sm = SimConnect()           # SimConnect instance
aq = AircraftRequests(sm)   # Used to get values from SimVars
db = SessionLocal()         # Database instance

no_sim = False              # Used to get out of the program's main loop when the plane is not moving on the ground

# **********************************************************************************************************************
#   Program
# **********************************************************************************************************************

try:
    # Creates a new flight with starting date and location
    current_flight = create_flight(db, datetime.now(), f"{aq.get("PLANE_LATITUDE")},{aq.get("PLANE_LONGITUDE")}",
                                   f"", None, None)
except Exception as e:
    print("Impossible de créer un nouveau vol, le simulateur n'est pas en marche.")
    no_sim = True

while not no_sim:
    try:
        insert_measurement(db, current_flight.Id)   # Creates a new measurement for the current flight

        if aq.get("GROUND_VELOCITY") < 3 and aq.get("PLANE_ALT_ABOVE_GROUND") < 3:
            # Updates the flight with ending date and location
            update_flight(db, current_flight.Id, None, None, None, datetime.now(),
                        f"{aq.get("PLANE_LATITUDE")},{aq.get("PLANE_LONGITUDE")}")
            break

        time.sleep(3.6)  # Waits 3.6 seconds before doing another measurement (takes approx. 1.4 seconds to execute)

    except Exception as e:
        print("Impossible d'enregistrer les données du vol, le simulateur n'est plus en marche")
        break

if not no_sim:
    get_data(current_flight.Id)    # Exports current flight data to csv file

sm.exit()