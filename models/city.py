#!/usr/bin/env python3
""" Declare a City Model that inherits
from the Base Model """
from models.base_model import BaseModel


class City(BaseModel):
    '''City Model'''
    state_id = ""
    name = ""
