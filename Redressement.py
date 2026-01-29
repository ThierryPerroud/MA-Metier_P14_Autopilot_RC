# Program name: Redressement.py
# Description: Ajusts the glider's roll to stabilize it
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 29.01.2026
# Version : 1.0

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from SimConnect import SimConnect, AircraftRequests
import time, math

# **********************************************************************************************************************
#   Variables
# **********************************************************************************************************************
sm = SimConnect()           # SimConnect instance
aq = AircraftRequests(sm)   # Used to get values from SimVars

# **********************************************************************************************************************
#   Functions
# **********************************************************************************************************************

def stabilize_roll(new_degrees):
    actual_roll = math.degrees(aq.get("PLANE_BANK_DEGREES")) - new_degrees
    if actual_roll is None:
        return
    rotation = 0.2
    if actual_roll < -0.5:
        aq.set("AILERON_POSITION", -rotation)
        print(f"corrige vers la gauche ({actual_roll}°)")
    elif actual_roll > 0.5:
        aq.set("AILERON_POSITION", rotation)
        print(f"corrige vers la droite ({actual_roll}°)")
    else:
        aq.set("AILERON_POSITION", 0)
        print(f"plutôt centré ({actual_roll}°)")


def stabilize_roll_precise(new_degrees):
    actual_roll =  math.degrees(aq.get("PLANE_BANK_DEGREES")) - new_degrees
    if actual_roll is None:
        return
    rotation = 0.025
    if actual_roll < -0.25:
        aq.set("AILERON_POSITION", -rotation)
        print(f"corrige vers la gauche ({actual_roll}°)")
    elif actual_roll > 0.25:
        aq.set("AILERON_POSITION", rotation)
        print(f"corrige vers la droite ({actual_roll}°)")
    else:
        aq.set("AILERON_POSITION", 0)
        print(f"plutôt centré ({actual_roll}°)")


def Start_stabilize(new_degrees=0):
    while True:
        actual_roll = aq.get("PLANE_BANK_DEGREES")
        if actual_roll is None:
            pass
        elif math.degrees(actual_roll) > 1 or math.degrees(actual_roll) < -1:
            stabilize_roll(new_degrees)
            print("roll normal")
        else:
            stabilize_roll_precise(new_degrees)
            print("roll précis")
            #break
        time.sleep(0.2)

Start_stabilize()