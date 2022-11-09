#!/usr/bin/env python3
'''Amenity Model Testing'''
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_attribute(unittest.TestCase):
    '''Unittests for Amenity Model'''

    def test_hasattr_name(self):
        new = Amenity()
        self.assertTrue('name' in dir(new))

    def test_name_type(self):
        self.assertIsInstance(Amenity.name, str)


class TestAmenity_inherit(unittest.TestCase):
    '''Unittests for Amenity inheritance'''

    def test_classname_in_str(self):
        self.assertIn('Amenity', Amenity().__str__())

    def test_id_in_str(self):
        self.assertIn('id', Amenity().__str__())

    def test_dict_method(self):
        self.assertIsInstance(Amenity().__dict__, dict)

    def test_no_args_init(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_is_str(self):
        self.assertIsInstance(Amenity().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(Amenity().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(Amenity().updated_at, datetime)

    def test_different_id(self):
        rat1 = Amenity()
        rat2 = Amenity()
        self.assertNotEqual(rat1.id, rat2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        um = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(um.id, "345")
        self.assertEqual(um.created_at, dt)
        self.assertEqual(um.updated_at, dt)

    def test_one_save(self):
        um = Amenity()
        sleep(0.05)
        first_updated_at = um.updated_at
        um.save()
        self.assertIsInstance(first_updated_at, datetime)
        self.assertNotEqual(type(um.updated_at), str)

    def test_save_with_arg(self):
        um = Amenity()
        with self.assertRaises(TypeError):
            um.save(None)

            self.assertIn(umid, f.read())

    def test_to_dict_type(self):
        um = Amenity()
        self.assertIsInstance(um.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        um = Amenity()
        um_dict = um.to_dict()
        self.assertEqual(str, type(um_dict["created_at"]))
        self.assertEqual(str, type(um_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        um = Amenity()
        um.id = "123456"
        um.created_at = um.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(um.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
