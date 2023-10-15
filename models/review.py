#!/usr/bin/python3

"""Module that defines the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """IMplement the Review class"""

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, Kwargs)
        place_id = ""
        user_id = ""
        text = ""
