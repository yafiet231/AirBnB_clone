#!/usr/bin/python3

"""This module defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel.
    Public class attribute:
    name:string- Name of the amenity.
    """
    name = ""
