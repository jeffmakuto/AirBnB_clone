#!/usr/bin/python3

"""
Modules for base model.
"""

from datetime import datetime
import json
import uuid
import models


class BaseModel:
    """
    class that defines all common attributes and methods for other classes.
    """
    def __init__(self, **kwargs):
        """Initialize a new BaseModel instance with the given attributes."""

        # Set a unique ID for the instance
        self.id = str(uuid.uuid4())

        # Set the creation and update dates to the current date and time
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Set the date string format
        tform = "%Y-%m-%dT%H:%M:%S.%f"

        # Update the instance attributes based on the given keyword arguments
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, tform))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        # Get the class name and instance ID
        clname = type(self).__name__
        instance_id = getattr(self, "id", None)
        # Get a dictionary of the instance attributes
        instance_attrs = vars(self).copy()
        # Remove any reserved attributes
        reserved_attrs = ["id", "created_at", "updated_at"]
        for attr in reserved_attrs:
            instance_attrs.pop(attr, None)
        # Format the string representation of the instance
        instance_attrs_str = ", ".join(f"{k}={v!r}"
                                       for k, v in instance_attrs.items())
        instance_str = f"[{clname}] ({instance_id}) {{{instance_attrs_str}}}"
        return instance_str

    def save(self):
        """
        Updates the attribute 'updated_at' to current date and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of instance of base model.
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
