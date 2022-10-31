#!/usr/bin/env python3
''' Contains the BaseModel Class '''
import datetime as dt
import uuid


class BaseModel:
    ''' BaseModel Class '''

    def __init__(self, *arg, **kwargs):
        ''' Initialising '''
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = dt.datetime.now()

    def __str__(self):
        ''' Should Print'''
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' updates the public instance attribute with the current datetime '''
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all
        keys/values of __dict__ of the instance '''
        n_dict = self.__dict__.copy()
        n_dict['__class__'] = self.__class__.__name__
        n_dict['updated_at'] = self.updated_at.isoformat()
        n_dict['created_at'] = self.created_at.isoformat()
        return n_dict
