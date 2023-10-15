#!/usr/bin/python3

"""
This module defines the State class inheriting from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a possible state for a location.

    Attributes:
        name (str): Name of the state.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
