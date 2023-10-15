#!/usr/bin/python3

""" FileStorage modules
"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ serializes instances to a JSON file and
        deserializes JSON file to instances

        private calss attributes:
            __file_path: string - path to JSON (ex: file.json)
            __objects: dictionary - empty but will store all objects
            by <class name>.id (ex: store a BaseModel object with
            id=121212, the key will be BaseModel.121212)

        public instance methods:
            all(self): returns the dictionary __objects
            new(self, obj): sets in __objects the obj
            save(self): serializes __objects to the JSON file(path: __file_path)
            reload(self): deserializes the JSON file to __objects (only if the
            JSON file (__file_path) exists; otherwise, do nothing. If the file
            doesn’t exist, no exception should be raised)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the object with key <obj cls name>.id """
        class_name = type(obj).__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to JSON file (path:__file_path) """
        obj_dict = FileStorage.__objects
        new_obj_dict = {obj: obj_dict[obj].to_dict() for obj in
                        obj_dict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_obj_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    class_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
