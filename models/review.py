#!/usr/bin/python3

"""This module defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel.

    Public class Attributes:
        place_id:string- Will be the Place.id.
        user_id:string- Will be the User.id.
        text:string- Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
