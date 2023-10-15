#!/usr/bin/python3

"""File Storage class rising from models"""
from json import loads, dump, dumps
from os.path import exists
from models import base_model
from models import user
from models import place
from models import state
from models import city
from models import amenity
from models import review

City = city.City
Amenity = amenity.Amenity
Place = place.Place
BaseModel = base_model.BaseModel
User = user.User
State = state.State
Review = review.Review

class_name = ["BaseModel",
              "City",
              "State",
              "Place",
              "Amenity",
              "Review",
              "User"]


class FileStorage:
    """
    Class for the file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the object with key into __objects{}
        """
        ind = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[ind] = obj

        def save(self):
        """
        Serializes __object to JSON file to path '__file_path'
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserialize JSON to __objects
        """
        if exists(FileStorage.__file_path):
            # Done if JSON file exists, recorded in file_path
            with open(FileStorage.__file_path, "r", encoding='utf-8') as doc:
                dict_from_json = json.load(doc)  # Corrected function name
            for key, value in dict_from_json.items():
                if key.split('.')[0] in name_class:
                    # Deserialize indices
                    FileStorage.__objects[key] = eval(key.split('.')[0])(**value)

