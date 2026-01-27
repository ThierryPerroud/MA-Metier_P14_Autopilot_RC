# Program name: CRUD.__init__.py
# Description: Transforms the CRUD directory into a package
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.3

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from .Gliders import *
from .Flights import *
from .Thermals import *
from .Configurations import *
from .gliders_has_flights import *
from .Telemetry_measurements import *

# **********************************************************************************************************************
#   Variables
# **********************************************************************************************************************
__all__ = [
    Gliders,
    Flights,
    Thermals,
    Configurations,
    gliders_has_flights,
    Telemetry_measurements,
]