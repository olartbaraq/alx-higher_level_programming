#!/usr/bin/python3
"""State class definition"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """ Class State that inherities from Base class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref=backref("state", cascade="all"),
                          single_parent=True)
