#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
""" Add a conditional depending of the value
    of the environment variable HBNB_TYPE_STORAGE """
from ..models.engine.file_storage import FileStorage
from ..models.base_model import BaseModel, Base
from ..models.user import User
from ..models.place import Place
from ..models.state import State
from ..models.city import City
from ..models.amenity import Amenity
from ..models.review import Review
from os import getenv
from ..models.engine.db_storage import DBStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
