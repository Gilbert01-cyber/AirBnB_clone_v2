#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """Stores objects in a MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine from environment variables."""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dict of objects, optionally filtered by class."""
        if cls is None:
            targets = list(classes.values())
        else:
            if isinstance(cls, str):
                cls = classes.get(cls)
            targets = [cls] if cls is not None else []
        result = {}
        for target in targets:
            if not hasattr(target, "__table__"):
                continue
            for obj in self.__session.query(target).all():
                result["{}.{}".format(type(obj).__name__, obj.id)] = obj
        return result

    def new(self, obj):
        """Add obj to the current session."""
        self.__session.add(obj)

    def save(self):
        """Commit the current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and the session."""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)
