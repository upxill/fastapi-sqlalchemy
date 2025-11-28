
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    DATABASE_URL, 
    connect_args={
        "check_same_thread": False
        }, 
    pool_size=10,        # Keep 10 connections in the pool
    max_overflow=2,      # Allow up to 2 extra connections temporarily
    pool_recycle=3600,   # Recycle connections after 1 hour
    pool_pre_ping=True )
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
