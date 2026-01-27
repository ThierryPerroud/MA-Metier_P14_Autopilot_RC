# Program name: Calculations.CalculDistance.py
# Description: Function to calculate the distance between the starting location and the destination location
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
import math

# **********************************************************************************************************************
#   Functions
# **********************************************************************************************************************

def distance_haversine(lat1, lon1, lat2, lon2):
    """
    Calcule la distance en kilomètres entre deux points (lat1, lon1) et (lat2, lon2)
    Utilise la formule de haversine (distance du grand cercle)
    """
    # Rayon de la Terre en km
    R = 6371.0

    # Convertir en radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Formule de haversine
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_km = R * c
    return distance_km