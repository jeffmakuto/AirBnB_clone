#!/usr/bin/python3

'''This module defines all common attributes/methods for other classes'''

import uuid
from datetime import datetime
import models


class BaseModel():
    ''' defines common attributes/methods for other classes

        Public Instance Attributes:
            id: (string) - assigned with an uuid when an instance is created.
            created_at: (datetime) - assigned with the current datetime when
                        an instance is created
            updated_at: (datetime) - assigned with the current datetime when
                        an instance is created and will be updated every time
                        the object changes
            __str__: prints: [<class name>] (<self.id>) <self.__dict__>

        Public Instance Methods:
            save(self): updates the public instance attribute updated_at with
                        the current datetime
            to_dict(self): returns a dictionary containing all keys/values of
                        __dict__ of the instance.
    '''
    def __init__(self, *args, **kwargs):
        ''' Instantiates objects '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            tform = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        ''' returns a formated string '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at with the
            current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            returns the dictionary of the BaseModel instance

            and the key/value pair of __class__ representing
            the class name of the object
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
