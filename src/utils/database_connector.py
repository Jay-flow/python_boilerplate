from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.abstracts.singleton import Singleton
from src.utils.env import get


class DatabaseConnector(metaclass=Singleton):
    def __init__(self):
        self.engin = create_engine(
            get('DATABASE_URL'),
            pool_pre_ping=True,
            echo=True
        )

    @property
    def session(self):
        return Session(self.engin)
