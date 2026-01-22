from Class.Thermals import Thermals
from sqlalchemy.orm import Session

def create_thermal(db: Session, strength: float, radius: float, glider_id: int):
    new_thermal = Thermals(
        Strength=strength,
        Radius=radius,
        glider_id=glider_id
    )
    db.add(new_thermal)
    db.commit()
    db.refresh(new_thermal)
    db.close()
    return new_thermal

def get_thermal(db: Session, thermal_id: int):
    return db.query(Thermals).filter(Thermals.Id == thermal_id).first()


def get_thermals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Thermals).offset(skip).limit(limit).all()

def delete_thermal(db: Session, thermal_id: int):
    thermal = db.query(Thermals).filter(Thermals.Id == thermal_id).first()
    if thermal:
        db.delete(thermal)
        db.commit()
        db.close()
    return thermal

def update_thermal(db: Session, thermal_id: int, strength: float = None, radius: float = None, glider_id: int = None):
    thermal = db.query(Thermals).filter(Thermals.Id == thermal_id).first()
    if thermal:
        if strength is not None:
            thermal.Strength = strength
        if radius is not None:
            thermal.Radius = radius
        if glider_id is not None:
            thermal.glider_id = glider_id
        db.commit()
        db.refresh(thermal)
        db.close()
    return thermal


def get_thermals_by_glider(db: Session, glider_id: int, skip: int = 0, limit: int = 100):
    return db.query(Thermals).filter(Thermals.glider_id == glider_id).offset(skip).limit(limit).all()