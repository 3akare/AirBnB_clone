#!/usr/bin/env python3
""" Declare a Review Model that inherits
from the Base Model """
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review Model'''
    place_id = ""
    user_id = ""
    text = ""
