from contextlib import asynccontextmanager
from typing import AsyncGenerator

from neo4j import GraphDatabase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings


# SQLAlchemy session factory (sync for simplicity in MVP)
engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Neo4j driver
neo4j_driver = GraphDatabase.driver(
    settings.neo4j_uri, auth=(settings.neo4j_username, settings.neo4j_password)
)


def get_neo4j_session():
    with neo4j_driver.session() as session:
        yield session


