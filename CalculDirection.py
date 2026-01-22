import math

def cap_vrai(lat1, lon1, lat2, lon2):
    """
    Calcule le cap VRAI d'un point A vers B
    MSFS convertira automatiquement en magnétique via PLANE_HEADING_MAGNETIC
    """
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_lambda = math.radians(lon2 - lon1)

    x = math.sin(delta_lambda) * math.cos(phi2)
    y = math.cos(phi1)*math.sin(phi2) - math.sin(phi1)*math.cos(phi2)*math.cos(delta_lambda)
    azimut_vrai = math.atan2(x, y)

    return (math.degrees(azimut_vrai) + 360) % 360