from SimConnect import SimConnect, AircraftRequests
import time, math

sm = SimConnect()
aq = AircraftRequests(sm)

def stabilize_roll(new_degrees=0):
    acutual_roll = math.degrees(aq.get("PLANE_BANK_DEGREES"))
    rotation = 0.2
    if acutual_roll < -5:
        aq.set("AILERON_POSITION", -rotation)
        print(f"corrige vers la gauche ({acutual_roll}°)")
    elif acutual_roll > 5:
        aq.set("AILERON_POSITION", rotation)
        print(f"corrige vers la droite ({acutual_roll}°)")
    else:
        aq.set("AILERON_POSITION", 0)
        print(f"plutôt centré ({acutual_roll}°)")

def stabilize_roll_precise(new_degrees=0):
    acutual_roll =  math.degrees(aq.get("PLANE_BANK_DEGREES"))
    rotation = 0.025
    if acutual_roll < -3:
        aq.set("AILERON_POSITION", -rotation)
        print(f"corrige vers la gauche ({acutual_roll}°)")
    elif acutual_roll > 3:
        aq.set("AILERON_POSITION", rotation)
        print(f"corrige vers la droite ({acutual_roll}°)")
    else:
        aq.set("AILERON_POSITION", 0)
        print(f"plutôt centré ({acutual_roll}°)")

def Start_stabilize():
    while True:
        actual_roll = aq.get("PLANE_BANK_DEGREES")
        if actual_roll is None:
            pass
        elif math.degrees(actual_roll) > 5 or math.degrees(actual_roll) < -5:
            stabilize_roll()
            print("roll normal")
        else:
            stabilize_roll_precise()
            print("roll précis")
            #break
        time.sleep(0.2)