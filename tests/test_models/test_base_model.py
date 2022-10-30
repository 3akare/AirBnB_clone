#!/usr/bin/env python3
''' BaseModel unittest Module'''

import unittest
from models.base_model import BaseModel
import datetime
import uuid


class BaseModelTest(unittest.TestCase):
    ''' Test for Instance'''

    def test_instance(self):
        """Test Intsance"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_datetime_creation(self):
        """checking for datetime function"""
        my_model = BaseModel()
        date = datetime.datetime.now()
        difference = my_model.updated_at - my_model.created_at
        self.assertTrue(abs(difference.total_seconds()) < 0.01)
        difference = my_model.created_at - date
        self.assertTrue(abs(difference.total_seconds()) < 0.1)


if __name__ == '__main__':
    unittest.main()
