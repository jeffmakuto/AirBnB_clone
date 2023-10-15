#!/usr/bin/python3

"""
module that defines city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Implements the City class"""

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        state_id = ""
        name = ""
