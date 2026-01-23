def get_pressure(SEA_LEVEL_PRESSURE, altitude):
    # Formula found on: https://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_variation
    altitude_in_meters = altitude * (0.3048/1)          # m
    LAPSE_RATE = 0.00976                                # K/m
    SEA_LEVEL_STANDARD_TEMP = 288.15                    # K
    GRAVITATIONAL_CONSTANT = 9.80665                    # m/s^2
    AIR_MOLAR_MASS = 0.02896968                         # kg/mol
    UNIVERSAL_GAS_CONSTANT = 8.314462618                # J/(mol*K)

    pressure = (SEA_LEVEL_PRESSURE * (1 + (LAPSE_RATE * altitude_in_meters) / SEA_LEVEL_STANDARD_TEMP)
                ** -((GRAVITATIONAL_CONSTANT * AIR_MOLAR_MASS) / (UNIVERSAL_GAS_CONSTANT * LAPSE_RATE)))

    return pressure