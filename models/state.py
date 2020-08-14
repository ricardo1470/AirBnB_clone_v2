#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ Update class State """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", passive_deletes=True, backref="state")

    @property
    def cities(self):
        """ Return all cities """
        cities = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                cities.append(city)
        return cities
