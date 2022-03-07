#!/usr/bin/python3
"""State class definition"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from model_state import Base


class City(Base):
        """ Class City that inherities from State class"""
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True,
                    nullable=False, unique=True, autoincrement=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
