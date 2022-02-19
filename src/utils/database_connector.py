from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.abstracts.singleton import Singleton
from src.utils.env import get


class DatabaseConnector(metaclass=Singleton):
    def __init__(self):
        self.engin = create_engine(
            get('DATABASE_URL'),
            echo=True
        )

        self.session = Session(self.engin)
