#!/usr/bin/env python3
""" Declare a Amenity Model that inherits
from the Base Model """
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity Model'''
    name = ""
