#!/usr/bin/env python3
''' Unittest for BaseModel'''
import unittest
from models.base_model import BaseModel
import datetime as dt


class TestBaseModel(unittest.TestCase):
    def test_base_init(self):
        ''' Test BaseModel init method '''

        md = BaseModel()
        md1 = BaseModel()
        self.assertIsInstance(md.id, str)
        self.assertIsInstance(md, BaseModel)
        md.save()
        self.assertNotEqual(md.created_at, md.updated_at)
        self.assertNotEqual(md1.id, md.id)


if __name__ == '__main__':
    unittest.main()
