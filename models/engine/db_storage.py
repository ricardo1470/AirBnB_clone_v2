#!/usr/bin/python3
"""this has the class for DBStorage"""

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData, create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """ database called DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ initialization of  DBStorage """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                           .format(user, password, host, db)
                                           pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    """ rev """
    def all(self, cls=None):
        """must return a dictionary: (like FileStorage)
            all elements in database"""
        if not self.__session:
            self.reload()
        database_dic = {}
        if cls is not None:
            objects = DBStorage.__session.query(cls).all()
            for objs in objects:
                key = "{}.{}".format(type(objs).__class__.__name__, objs.id)
                database_dic[key] = objs
            return database_dic
        else:
            for objs in DBStorage.__session.query(City,
                                                  State,
                                                  User,
                                                  Place,
                                                  Review,
                                                  Amenity).all():
                key = "{}.{}".format(type(objs).__class__.__name__, objs.id)
                database_dic[key] = objs
            return database_dic

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create tables """

        Base.metadata.create_all(DBStorage.__engine)
        session = sessionmaker(bind=DBStorage.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        DBStorage.__session = Session()
