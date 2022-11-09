#!/usr/bin/env python3
'''Place Model Testing'''
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_attribute(unittest.TestCase):
    '''Unittests for Place Model'''

    def test_hasattr_name(self):
        new = Place()
        self.assertTrue('name' in dir(new))

    def test_hasattr_city_id(self):
        new = Place()
        self.assertTrue('city_id' in dir(new))

    def test_hasattr_user_id(self):
        new = Place()
        self.assertTrue('user_id' in dir(new))

    def test_hasattr_description(self):
        new = Place()
        self.assertTrue('description' in dir(new))

    def test_hasattr_number_rooms(self):
        new = Place()
        self.assertTrue('number_rooms' in dir(new))

    def test_hasattr_number_bathrooms(self):
        new = Place()
        self.assertTrue('number_bathrooms' in dir(new))

    def test_hasattr_max_guest(self):
        new = Place()
        self.assertTrue('max_guest' in dir(new))

    def test_hasattr_price_by_night(self):
        new = Place()
        self.assertTrue('price_by_night' in dir(new))

    def test_hasattr_latitude(self):
        new = Place()
        self.assertTrue('latitude' in dir(new))

    def test_hasattr_longitude(self):
        new = Place()
        self.assertTrue('longitude' in dir(new))

    def test_name_type(self):
        self.assertIsInstance(Place.name, str)

    def test_city_id_type(self):
        self.assertIsInstance(Place.city_id, str)

    def test_user_id_type(self):
        self.assertIsInstance(Place.user_id, str)

    def test_description_type(self):
        self.assertIsInstance(Place.description, str)

    def test_number_rooms_type(self):
        self.assertIsInstance(Place.number_rooms, int)

    def test_number_bathrooms_type(self):
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_max_guest_type(self):
        self.assertIsInstance(Place.max_guest, int)

    def test_price_by_night_type(self):
        self.assertIsInstance(Place.price_by_night, int)

    def test_longitude_type(self):
        self.assertIsInstance(Place.longitude, float)

    def test_latitude_type(self):
        self.assertIsInstance(Place.latitude, float)

    def test_amenity_ids_type(self):
        self.assertIsInstance(Place.amenity_ids, str)


class TestPlace_inherit(unittest.TestCase):
    '''Unittests for Place inheritance'''

    def test_classname_in_str(self):
        self.assertIn('Place', Place().__str__())

    def test_id_in_str(self):
        self.assertIn('id', Place().__str__())

    def test_dict_method(self):
        self.assertIsInstance(Place().__dict__, dict)

    def test_no_args_init(self):
        self.assertEqual(Place, type(Place()))

    def test_id_is_str(self):
        self.assertIsInstance(Place().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(Place().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(Place().updated_at, datetime)

    def test_different_id(self):
        rat1 = Place()
        rat2 = Place()
        self.assertNotEqual(rat1.id, rat2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        um = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(um.id, "345")
        self.assertEqual(um.created_at, dt)
        self.assertEqual(um.updated_at, dt)

    def test_one_save(self):
        um = Place()
        sleep(0.05)
        first_updated_at = um.updated_at
        um.save()
        self.assertIsInstance(first_updated_at, datetime)
        self.assertNotEqual(type(um.updated_at), str)

    def test_save_with_arg(self):
        um = Place()
        with self.assertRaises(TypeError):
            um.save(None)

            self.assertIn(umid, f.read())

    def test_to_dict_type(self):
        um = Place()
        self.assertIsInstance(um.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        um = Place()
        um_dict = um.to_dict()
        self.assertEqual(str, type(um_dict["created_at"]))
        self.assertEqual(str, type(um_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        um = Place()
        um.id = "123456"
        um.created_at = um.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(um.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
