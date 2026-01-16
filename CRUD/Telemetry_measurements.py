from sqlalchemy.orm import Session
from Class import Telemetry_measurements


# CREATE - Créer une nouvelle mesure de télémétrie
def create_measurement(db: Session, timestamp: str, latitude: float, longitude: float,
                       altitude: int, altitude_agl: int, indicated_airspeed: float,
                       ground_speed: float, pitch: float, roll: float, yaw: float,
                       vario: float, g_factor: float, wind_direction: int,
                       wind_force: float, temperature: float, pression: float, flight_id: int):
    new_measurement = Telemetry_measurements(
        Timestamp=timestamp,
        Latitude=latitude,
        Longitude=longitude,
        Altitude=altitude,
        Altitude_agl=altitude_agl,
        Indicated_airspeed=indicated_airspeed,
        Ground_speed=ground_speed,
        Pitch=pitch,
        Roll=roll,
        Yaw=yaw,
        Vario=vario,
        G_factor=g_factor,
        Wind_direction=wind_direction,
        Wind_force=wind_force,
        Temperature=temperature,
        Pression=pression,
        Flight_id=flight_id
    )
    db.add(new_measurement)
    db.commit()
    db.refresh(new_measurement)
    return new_measurement


# READ - Lire une mesure par son ID
def get_measurement(db: Session, measurement_id: int):
    return db.query(Telemetry_measurements).filter(Telemetry_measurements.Id == measurement_id).first()


# READ - Lire toutes les mesures
def get_all_measurements(db: Session):
    return db.query(Telemetry_measurements).all()


# READ - Lire toutes les mesures d'un vol spécifique
def get_measurements_by_flight(db: Session, flight_id: int):
    return db.query(Telemetry_measurements).filter(Telemetry_measurements.Flight_id == flight_id).all()


# UPDATE - Modifier une mesure
def update_measurement(db: Session, measurement_id: int, **kwargs):
    measurement = db.query(Telemetry_measurements).filter(Telemetry_measurements.Id == measurement_id).first()

    if measurement:
        for key, value in kwargs.items():
            if value is not None and hasattr(measurement, key):
                setattr(measurement, key, value)

        db.commit()
        db.refresh(measurement)

    return measurement


# DELETE - Supprimer une mesure
def delete_measurement(db: Session, measurement_id: int):
    measurement = db.query(Telemetry_measurements).filter(Telemetry_measurements.Id == measurement_id).first()

    if measurement:
        db.delete(measurement)
        db.commit()
        return True

    return False


# DELETE - Supprimer toutes les mesures d'un vol
def delete_measurements_by_flight(db: Session, flight_id: int):
    measurements = db.query(Telemetry_measurements).filter(Telemetry_measurements.Flight_id == flight_id).all()

    if measurements:
        for m in measurements:
            db.delete(m)
        db.commit()
        return True

    return False


# EXEMPLE D'UTILISATION
if __name__ == "__main__":
    from Class.database import SessionLocal

    db = SessionLocal()

    # CREATE - Créer une mesure
    mesure = create_measurement(
        db=db,
        timestamp="2026-01-15 14:30:00",
        latitude=46.5197,
        longitude=6.6323,
        altitude=1500,
        altitude_agl=500,
        indicated_airspeed=80.5,
        ground_speed=85.2,
        pitch=5.2,
        roll=-2.1,
        yaw=180.0,
        vario=2.5,
        g_factor=1.2,
        wind_direction=270,
        wind_force=15.5,
        temperature=18.5,
        pression=1013.25,
        flight_id=1
    )
    print(f"Créé: {mesure}")

    # READ - Lire une mesure
    mesure = get_measurement(db, mesure.Id)
    print(f"Lu: {mesure}")

    # READ - Lire toutes les mesures d'un vol
    mesures_vol = get_measurements_by_flight(db, flight_id=1)
    print(f"Mesures du vol 1: {mesures_vol}")

    # UPDATE - Modifier une mesure
    mesure = update_measurement(db, mesure.Id, Altitude=1550, Vario=3.0)
    print(f"Modifié: {mesure}")

    # DELETE - Supprimer une mesure
    supprime = delete_measurement(db, mesure.Id)
    print(f"Supprimé: {supprime}")

    db.close()