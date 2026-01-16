from Class.Configurations import Configurations
from sqlalchemy.orm import Session

def create_configuration(db: Session, name: str, value: str):
    new_configuration = Configurations(
        Name=name,
        Value=value
    )
    db.add(new_configuration)
    db.commit()
    db.refresh(new_configuration)
    return new_configuration

def get_configuration(db: Session, config_id: int):
    return db.query(Configurations).filter(Configurations.Id == config_id).first()

def get_all_configurations(db: Session):
    return db.query(Configurations).all()

def update_configuration(db: Session, config_id: int, name: str = None, value: str = None):
    configuration = db.query(Configurations).filter(Configurations.Id == config_id).first()

    if configuration:
        if name:
            configuration.Name = name
        if value:
            configuration.Value = value

        db.commit()
        db.refresh(configuration)

    return configuration

def delete_configuration(db: Session, config_id: int):
    configuration = db.query(Configurations).filter(Configurations.Id == config_id).first()

    if configuration:
        db.delete(configuration)
        db.commit()
        return True

    return False

def example_usage(db: Session):
    # CREATE
    config = create_configuration(db, "MaxSpeed", "250")
    print(f"Created Configuration: {config.Id}, {config.Name}, {config.Value}")

    # READ
    fetched_config = get_configuration(db, config.Id)
    print(f"Fetched Configuration: {fetched_config.Id}, {fetched_config.Name}, {fetched_config.Value}")

    # UPDATE
    updated_config = update_configuration(db, config.Id, value="300")
    print(f"Updated Configuration: {updated_config.Id}, {updated_config.Name}, {updated_config.Value}")

    # DELETE
    if delete_configuration(db, config.Id):
        print(f"Deleted Configuration with ID: {config.Id}")
    else:
        print(f"Configuration with ID: {config.Id} not found for deletion.")