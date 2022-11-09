#!/usr/bin/env python3
""" Declare a User Model that inherits
from the Base Model """
from models.base_model import BaseModel


class User(BaseModel):
    '''User Model'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
