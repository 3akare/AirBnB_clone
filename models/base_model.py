#!/usr/bin/env python3
''' Contains the BaseModel Class '''
from datetime import datetime
import uuid


tf = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    ''' BaseModel Class '''

    def __init__(self, *arg, **kwargs):
        ''' Initialising '''

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                        kwargs["created_at"], tf)
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                        kwargs["updated_at"], tf)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' Should Print'''
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' updates the public instance attribute with the current datetime '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all
        keys/values of __dict__ of the instance '''
        n_dict = self.__dict__.copy()
        n_dict['__class__'] = self.__class__.__name__
        n_dict['updated_at'] = self.updated_at.isoformat()
        n_dict['created_at'] = self.created_at.isoformat()
        return n_dict
