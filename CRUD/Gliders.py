from sqlalchemy.orm import Session
from Class import Gliders


# CREATE - Créer un nouveau planeur
def create_glider(db: Session, model: str, empty_weight: int, center_gravity: float):
    new_glider = Gliders(
        Model=model,
        Empty_weight=empty_weight,
        Center_gravity=center_gravity
    )
    db.add(new_glider)
    db.commit()
    db.refresh(new_glider)
    return new_glider


# READ - Lire un planeur par son ID
def get_glider(db: Session, glider_id: int):
    return db.query(Gliders).filter(Gliders.Id == glider_id).first()


# READ - Lire tous les planeurs
def get_all_gliders(db: Session):
    return db.query(Gliders).all()


# UPDATE - Modifier un planeur
def update_glider(db: Session, glider_id: int, model: str = None,
                  empty_weight: int = None, center_gravity: float = None):
    glider = db.query(Gliders).filter(Gliders.Id == glider_id).first()

    if glider:
        if model:
            glider.Model = model
        if empty_weight:
            glider.Empty_weight = empty_weight
        if center_gravity:
            glider.Center_gravity = center_gravity

        db.commit()
        db.refresh(glider)

    return glider


# DELETE - Supprimer un planeur
def delete_glider(db: Session, glider_id: int):
    glider = db.query(Gliders).filter(Gliders.Id == glider_id).first()

    if glider:
        db.delete(glider)
        db.commit()
        return True

    return False


# EXEMPLE D'UTILISATION
if __name__ == "__main__":
    from Class.database import SessionLocal

    db = SessionLocal()

    # CREATE - Créer
    planeur = create_glider(db, "ASK-21", 360, 0.28)
    print(f"Créé: {planeur}")

    # READ - Lire
    planeur = get_glider(db, planeur.Id)
    print(f"Lu: {planeur}")

    # READ ALL - Lire tous
    tous = get_all_gliders(db)
    print(f"Tous: {tous}")

    # UPDATE - Modifier
    planeur = update_glider(db, planeur.Id, empty_weight=365)
    print(f"Modifié: {planeur}")

    # DELETE - Supprimer
    supprime = delete_glider(db, planeur.Id)
    print(f"Supprimé: {supprime}")

    db.close()