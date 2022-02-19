from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


from src.utils.database_connector import DatabaseConnector

Base: DeclarativeMeta = declarative_base()


class SampleModel(Base):
    __tablename__ = 'Video'
    id = Column(BIGINT(20, unsigned=True), primary_key=True,
                autoincrement=True, nullable=False)

    createdAt = Column(TIMESTAMP, nullable=False,
                       comment='Creation date', default=datetime.now())
    updatedAt = Column(TIMESTAMP, nullable=False,
                       comment='Update date', default=datetime.now())
    deletedAt = Column(TIMESTAMP, nullable=True, comment='Delete date')


if __name__ == '__main__':
    db = DatabaseConnector()

    try:
        option = input('column[c/r/d] : ').lower()

        if option == 'c':
            Base.metadata.create_all(db.engin)
        elif option == 'r':
            Base.metadata.drop_all(db.engin)
            Base.metadata.create_all(db.engin)
        elif option == 'd':
            Base.metadata.drop_all(db.engin)
        else:
            print('Wrong input value. Please try again.')
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()
