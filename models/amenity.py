#!/usr/bin/bash

""" Modules for Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represent the Amenity class."""

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **kwargs)
        name = ""
