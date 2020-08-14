#!/usr/bin/python3
"""this has the class for DBStorage"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import hashlib


# TODO Create class DBStorage and empty methods
class DBStorage:
    """
     Class DBStorage
    """

    __engine = None
    __session = None
    __tables = [
        "User",
        "State",
        "City",
        "Place",
        "Review",
        "Amenity"
    ]

    def __init__(self):
        """ Initilize the db storage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            """ Drop all tables"""
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """  Shows all rows in a table
        """
        results = {}
        if cls is not None:
            # TODO cls always is a class
            if type(cls) == str:
                cls = eval(cls)
            for instance in self.__session.query(cls):
                key = "{}.{}".format(cls.__name__, instance.id)
                results[key] = instance
            return results
        else:
            for table in self.__tables:
                for instance in self.__session.query(eval(table)):
                    key = "{}.{}".format(table, instance.id)
                    results[key] = instance
            return results

    def new(self, obj):
        """ Creates a new rigister
        """
        self.__session.add(obj)

    def save(self):
        """ Saves all current changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Removes an register
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads dabatase session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close connection
        """
        self.__session.close()
