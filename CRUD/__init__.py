# Program name: CRUD.__init__.py
# Description: Transforms the CRUD directory into a package
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.4

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
    "create_configuration",
    "get_configuration",
    "get_all_configurations",
    "update_configuration",
    "delete_configuration",
    "create_flight",
    "get_flight",
    "get_all_flights",
    "update_flight",
    "delete_flight",
    "create_glider",
    "get_glider",
    "get_all_gliders",
    "update_glider",
    "delete_glider",
    "create_measurement",
    "get_measurement",
    "get_all_measurements",
    "get_measurements_by_flight",
    "update_measurement",
    "delete_measurement",
    "delete_measurements_by_flight",
    "create_thermal",
    "get_thermal",
    "get_thermals",
    "delete_thermal",
    "update_thermal",
    "get_thermals_by_glider"
]