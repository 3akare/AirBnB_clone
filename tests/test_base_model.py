#!/usr/bin/env python3
''' Base Model Testing '''
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    ''' Test Case for BaseModel from models '''

    def test_init(self):
        ''' Init Test'''

        lab_rat = BaseModel()
        self.assertIsInstance(lab_rat, BaseModel)

    def test_save(self):
        ''' save() Test'''

        lab_rat = BaseModel()
        old_time = lab_rat.updated_at
        lab_rat.save()
        new_time = lab_rat.updated_at
        self.assertNotEqual(old_time, new_time)

    def test_to_dict(self):
        ''' to_dict() Test '''

        lab_rat = BaseModel()
        lab_rat_json = lab_rat.to_dict()
        self.assertIsInstance(lab_rat_json, dict)
        for key, values in lab_rat_json.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(values, str)

    def test_self_id(self):
        ''' self_id Test '''

        lab_rat = BaseModel()
        lab_rat_len = len(lab_rat.id)
        new = uuid.uuid4()
        new_len = len(str(new))
        self.assertIsInstance(lab_rat.id, str)
        self.assertEqual(new_len, lab_rat_len)

    def test_self_created_at(self):
        ''' self_created_at Test '''

        lab_rat = BaseModel()
        self.assertIsInstance(lab_rat.created_at, datetime.datetime)

    def test__str__(self):
        ''' String Representation Test '''

        lab_rat = BaseModel()
        string = lab_rat.__str__
        self.assertNotIsInstance(string, str)
