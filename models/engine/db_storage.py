#!/usr/bin/python3
"""this has the class for DBStorage"""
import models
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from ..models.base_model import BaseModel, Base
from ..models.user import User
from ..models.place import Place
from ..models.state import State
from ..models.city import City
from ..models.amenity import Amenity
from ..models.review import Review


class DBStorage:
    """ Databse storage Attributes """
    __engine = None
    __session = None

    def __init__(self):
        """ Instance attribute for DBStorage """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        pass

    def new(self, obj):
        """ creating new object """
        self.__session.add(obj)

    def save(self):
        """saving session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delets obj in session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ relad session """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the private session attribute"""
        if self.__session:
            self.__session.remove()
