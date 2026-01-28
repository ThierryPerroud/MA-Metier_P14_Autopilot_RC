# Program name: Calculations.__init__.py
# Description: Transforms the Calculations directory into a package
# Created by: Thierry Perroud
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.3

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from .CalculDirection import *
from .CalculDistance import *
from .CalculPressure import *
from .CalculWind import *

# **********************************************************************************************************************
#   Variables
# **********************************************************************************************************************
__all__ = [
    "cap_vrai",
    "distance_haversine",
    "get_pressure",
    "get_wind_speed",
    "get_wind_direction"
]