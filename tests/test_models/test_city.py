#!/usr/bin/env python3
'''City Model Testing'''
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_attribute(unittest.TestCase):
    '''Unittests for City Model'''

    def test_hasattr_state_id(self):
        new = City()
        self.assertTrue('state_id' in dir(new))

    def test_hasattr_name(self):
        new = City()
        self.assertTrue('name' in dir(new))

    def test_email_type(self):
        self.assertIsInstance(City.state_id, str)

    def test_first_name_type(self):
        self.assertIsInstance(City.name, str)


class TestCity_inherit(unittest.TestCase):
    '''Unittests for City inheritance'''

    def test_classname_in_str(self):
        self.assertIn('City', City().__str__())

    def test_id_in_str(self):
        self.assertIn('id', City().__str__())

    def test_dict_method(self):
        self.assertIsInstance(City().__dict__, dict)

    def test_no_args_init(self):
        self.assertEqual(City, type(City()))

    def test_id_is_str(self):
        self.assertIsInstance(City().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(City().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(City().updated_at, datetime)

    def test_different_id(self):
        rat1 = City()
        rat2 = City()
        self.assertNotEqual(rat1.id, rat2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        um = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(um.id, "345")
        self.assertEqual(um.created_at, dt)
        self.assertEqual(um.updated_at, dt)

    def test_one_save(self):
        um = City()
        sleep(0.05)
        first_updated_at = um.updated_at
        um.save()
        self.assertIsInstance(first_updated_at, datetime)
        self.assertNotEqual(type(um.updated_at), str)

    def test_save_with_arg(self):
        um = City()
        with self.assertRaises(TypeError):
            um.save(None)
            self.assertIn(umid, f.read())

    def test_to_dict_type(self):
        um = City()
        self.assertIsInstance(um.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        um = City()
        um_dict = um.to_dict()
        self.assertEqual(str, type(um_dict["created_at"]))
        self.assertEqual(str, type(um_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        um = City()
        um.id = "123456"
        um.created_at = um.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(um.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
