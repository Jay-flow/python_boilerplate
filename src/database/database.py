from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from src.abstracts.singleton import Singleton
from sqlalchemy.orm import sessionmaker
from env import DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER_NAME, DATABASE_NAME, RDBMS


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.engin = self.__create_engin()

    def __create_engin(self) -> Engine:
        return create_engine(
            f"{RDBMS}://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}",
            echo=True
        )
