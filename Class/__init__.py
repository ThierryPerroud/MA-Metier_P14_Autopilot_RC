# Program name: Class.__init__.py
# Description: Transforms the Class directory into a package
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from .database import *
from .Configurations import *
from .Flights import *
from .Thermals import *
from .Gliders import *
from .Telemetry_measurements import *
from .gliders_has_flights import *

# **********************************************************************************************************************
#   Variables
# **********************************************************************************************************************
__all__ = [
    database,
    Configurations,
    Flights,
    Thermals,
    Gliders,
    Telemetry_measurements,
    gliders_has_flights
]