#!/usr/bin/env python3
""" Declare a Base Model """
import models
import datetime
import uuid


class BaseModel:
    """ Base Model """

    def __init__(self, *args, **kwargs):
        ''' init instance '''
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) != 0 or kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        ''' String Magic Method '''

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' Updates the pubic instance attribute with current datetime '''

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Returns a dictionary conatining all
        keys/values of __dict__ of the instance
        '''

        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = str(self.created_at.isoformat())
        new_dict['updated_at'] = str(self.updated_at.isoformat())
        return new_dict
