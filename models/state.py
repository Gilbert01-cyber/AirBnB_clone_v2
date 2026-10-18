#!/usr/bin/python3
"""Defines the State class."""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Represents a State."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """Return the City instances linked to this State."""
            import models
            return [obj for obj in models.storage.all().values()
                    if type(obj).__name__ == "City"
                    and obj.state_id == self.id]
