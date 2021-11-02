from sqlalchemy.ext.declarative import declarative_base
from src.database.database import Database
from sqlalchemy import Column, Integer


Base = declarative_base()


class SampleModel(Base):  # type: ignore
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True)


if __name__ == '__main__':
    option = input('column[c/r/d] : ')
    db = Database()
    if option == 'c':
        Base.metadata.create_all(db.engin)
    elif option == 'r':
        Base.metadata.drop_all(db.engin)
        Base.metadata.create_all(db.engin)
    elif option == 'd':
        Base.metadata.drop_all(db.engin)
    else:
        print('Wrong input value. Please try again.')
