from SimConnect import SimConnect, AircraftRequests
import time

def stabilize_roll():
    acutual_roll = aq.get("PLANE_BANK_DEGREES")