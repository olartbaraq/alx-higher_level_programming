#!/usr/bin/python3
"""City model ORM"""

from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from model_state import Base


class City(Base):
    """City class declaration"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
