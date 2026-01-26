from sqlalchemy.orm import Session
from Class import Flights

# CREATE - Créer un nouveau vol
def create_flight(db: Session, Starting_date: str, Starting_location: str, Destination_location: str, Ending_date: str, Ending_location: str):
    new_flight = Flights(
        Starting_date=Starting_date,
        Starting_location=Starting_location,
        Destination_location=Destination_location,
        Ending_date=Ending_date,
        Ending_location=Ending_location,
    )
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    db.close()
    return new_flight

# READ - Lire un vol par son ID
def get_flight(db: Session, flight_id: int):
    return db.query(Flights).filter(Flights.Id == flight_id).first()

# READ - Lire tous les vols
def get_all_flights(db: Session):
    return db.query(Flights).all()

# UPDATE - Modifier un vol
def update_flight(db: Session, flight_id: int, Starting_date: str = None, Starting_location: str = None, Destination_location: str = None,
                  Ending_date: str = None, Ending_location: str = None):
    flight = db.query(Flights).filter(Flights.Id == flight_id).first()
    if flight:
        if Starting_date:
            flight.Starting_date = Starting_date
        if Starting_location:
            flight.Starting_location = Starting_location
        if Destination_location:
            flight.Destination_location = Destination_location
        if Ending_date:
            flight.Ending_date = Ending_date
        if Ending_location:
            flight.Ending_location = Ending_location
        db.commit()
        db.refresh(flight)
        db.close()
    return flight

# DELETE - Supprimer un vol
def delete_flight(db: Session, flight_id: int):
    flight = db.query(Flights).filter(Flights.Id == flight_id).first()

    if flight:
        db.delete(flight)
        db.commit()
        db.close()
        return True

    return False

# EXEMPLE D'UTILISATION
if __name__ == "__main__":
    from Class.database import SessionLocal

    db = SessionLocal()

    # CREATE - Créer
    vol = create_flight(db, "2026-01-15 14:00:00", "2026-01-15 15:00:00")
    print(f"Créé: {vol}")

    # READ - Lire
    vol = get_flight(db, vol.Id)
    print(f"Lu: {vol}")

    # READ ALL - Lire tous
    tous = get_all_flights(db)
    print(f"Tous: {tous}")

    # UPDATE - Modifier
    vol = update_flight(db, vol.Id, Ending_date="2026-01-15 14:45:00")
    print(f"Modifié: {vol}")

    # DELETE - Supprimer
    supprime = delete_flight(db, vol.Id)
    print(f"Supprimé: {supprime}")

    db.close()