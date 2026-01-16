from Class.database import *
from Class.Configurations import *
from Class.Flights import *
from Class.Thermals import *
from Class.Gliders import *
from Class.Telemetry_measurements import *
from Class.gliders_has_flights import *

#Utilise les class pour créer un BDD
Base.metadata.create_all(bind=engine)