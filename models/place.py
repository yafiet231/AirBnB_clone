#!/usr/bin/python3

"""This module defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Public class Attributes:
        city_id:string- Id of a city.
        user_id:string- Id of a user
        name:string- Name of a place.
        description:string- Description about a place.
        number_rooms:integer- Number of rooms of a place.
        number_bathrooms:integer- Number of bathrooms of a place.
        max_guest:integer- Maximum number of guests of a place.
        price_by_night:integer- Price by night of a place.
        latitude:float- Latitude of a place.
        longitude:float- Longitude of a place.
        amenity_ids:list- Will be the list of Amenity.id later
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
