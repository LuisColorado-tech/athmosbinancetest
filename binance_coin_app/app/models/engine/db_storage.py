from os import getenv
import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    ...
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        ...
        """
        self.__engine = create_engine(
            f'{getenv("POSTGRES_DATABASE_URL")}'
        )

    def new(self, obj):
        """
        ...
        """
        self.__session = sessionmaker(bind=self.__engine)
        if obj:
            self.__session.add(obj)
            self.__session.commit()
