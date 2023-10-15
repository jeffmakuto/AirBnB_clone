#!/usr/bin/python3

"""modules that defines a Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implements the place model

    Args:
        city_id (str): City id.
        user_id (str): User id.
        name (str): Name of the place.
        description (str): The description of the place.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bath bathrooms of place.
        max_guest (int): Maximum number of guest of place.
        price_by_night (int): Price for each night spent.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        amenity_ids (list): A list of the anemity ids.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        city_id = ""
        user_id = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
