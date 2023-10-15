#!/usr/bin/python3

"""
This module defines the User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user object.

    Attributes:
        email (str): Email of user.
        first_name (str): First name of user.
        last_name (str): Last name of user.
        password (str): Plain text passcode for user.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""
