# Program name: Class.database.py
# Description: Uses the SQLAlchemy ORM to create our database
# Created by: Jason Edmonds
# Last modified by: Thierry Perroud
# Last Modified date: 27.01.2026
# Version : 0.2

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# **********************************************************************************************************************
#   Variables
# **********************************************************************************************************************
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

# **********************************************************************************************************************
#   Functions
# **********************************************************************************************************************

def Session():
    """Retourne une nouvelle Session SQLAlchemy (factory)."""
    return SessionLocal()