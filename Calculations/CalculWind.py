# Program name: Calculations.CalculWind.py
# Description: Functions to calculate the wind's direction and speed
# Created by: Thierry Perroud
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

def get_wind_speed(wind_x, wind_y, wind_z):
    # Vitesse en m/s
    speed = math.sqrt(wind_x**2 + wind_y**2 + wind_z**2)

    return speed


def get_wind_direction(wind_x, wind_z, yaw):
    # Direction du vent en 2D (axe horizontal et longitudal
    direction_radian = math.atan2(-wind_x, -wind_z)             # Direction du vent en Radian (relative au planeur)
    direction_degree = (math.degrees(direction_radian) + 360)   # Direction du vent en Degrés (relative au planeur)
    yaw_in_degrees = math.degrees(yaw)                          # Orientation du planeur
    wind_direction = (direction_degree + yaw_in_degrees) % 360  # Direction du vent en degrés (relative au nord magnétique)

    return wind_direction