#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Class for amenity. Used in console.py"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
