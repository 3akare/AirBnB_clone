#!/usr/bin/env python3
""" Declare a Base Model """
import datetime
import uuid


class BaseModel:
    """ Base Model """

    def __init__(self, *args, **kwargs):
        ''' init instance '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        ''' String Magic Method '''

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' Updates the pubic instance attribute with current datetime '''

        self.updated_at = datetime.datetime.now()

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
