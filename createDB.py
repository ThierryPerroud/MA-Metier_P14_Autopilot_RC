# Program name: createDB.py
# Description: Creates empty database.db file using Class.database.py and all Table classes
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from Class.database import *
from Class.Configurations import *
from Class.Flights import *
from Class.Thermals import *
from Class.Gliders import *
from Class.Telemetry_measurements import *
from Class.gliders_has_flights import *

# **********************************************************************************************************************
#   Program
# **********************************************************************************************************************
#Utilise les class pour créer un BDD
Base.metadata.create_all(bind=engine)