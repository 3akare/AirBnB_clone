#!/usr/bin/env python3
''' Module contains Base Model class '''


import datetime as dt
import uuid

class BaseModel:
    ''' Representation of a base model'''

    def __init__(self, *args, **kwargs):
        ''' Initialising Object'''
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = dt.datetime.now()

    def save(self):
        ''' Updates the pubic instance attribute with the current datetime'''
        self.updated_at = dt.datetime.now().isoformat()

    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of __dict__ of the instance'''

        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = dt.datetime.now().isoformat()
        dic["updated_at"] = dt.datetime.now().isoformat()
        return dic

    def __str__(self):
        """ Print a Base Model """
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)
