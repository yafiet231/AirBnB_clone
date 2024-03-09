#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class which derives from BaseModel."""
    state_id = ""
    name = ""
