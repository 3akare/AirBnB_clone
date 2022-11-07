#!/usr/bin/env python3
''' Base Model Testing '''
import unittest
from datetime import datetime
from time import sleep
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


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()
