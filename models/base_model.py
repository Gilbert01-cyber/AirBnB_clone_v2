#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all AirBnB clone models.

    Defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel, or recreate one from kwargs.

        Args:
            *args: unused.
            **kwargs: key/value pairs to recreate an instance from a
                dictionary representation (e.g. from to_dict()).
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current time and persist to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
