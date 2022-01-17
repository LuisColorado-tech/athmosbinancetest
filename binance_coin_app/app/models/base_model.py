from sqlalchemy.ext.declarative import declarative_base
from .__init__ import storage

Base = declarative_base()


class BaseModel:

    def save(self):
        """
        Save the object to the db
        """
        storage.new(self)
