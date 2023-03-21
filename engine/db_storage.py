#!/usr/bin/python3
"""model mange DB"""
import models
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Initialize class nad use SQLAlchemy"""

    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """init"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all function"""
        dict_new = {}
        if cls is None:
            for c in self.all_classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    dict_new[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__+'.' + instance.id
                dict_new[key] = instance

        return dict_new

    def new(self, obj):
        """new instance db storage"""
        self.__session.add(obj)

    def save(self):
        """save instance db storage"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete instance db storage"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create table in database"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def close(self):
        """closing the session"""
        self. reload()
        self.__session.close()
