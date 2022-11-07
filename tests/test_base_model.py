#!/usr/bin/env python3
''' Base Model Testing '''
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    ''' Test Case for BaseModel init '''

    def test_no_args_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))
    
    def test_id_is_str(self):
        self.assertIsInstance(BaseModel().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(BaseModel().updated_at, datetime)
    
    def test_different_id(self):
        rat1 = BaseModel()
        rat2 = BaseModel()
        self.assertNotEqual(rat1.id, rat2.id)

