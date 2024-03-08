#!/usr/bin/python3

"""This module defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel.

    Public Class Attributes:
        email:string- Email address of a user.
        password:string- Password of a user.
        first_name:string- First name of a user.
        last_name:string- Last name of a user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
