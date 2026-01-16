from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///database.db"

# Base pour tous les modèles
Base = declarative_base()

# Engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

# Session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

def Session():
    """Retourne une nouvelle Session SQLAlchemy (factory)."""
    return SessionLocal()