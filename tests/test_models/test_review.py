#!/usr/bin/env python3
'''Review Model Testing'''
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_attribute(unittest.TestCase):
    '''Unittests for Review Model'''

    def test_hasattr_place_id(self):
        new = Review()
        self.assertTrue('place_id' in dir(new))

    def test_hasattr_user_id(self):
        new = Review()
        self.assertTrue('user_id' in dir(new))

    def test_hasattr_text(self):
        new = Review()
        self.assertTrue('text' in dir(new))

    def test_name_place_id_type(self):
        self.assertIsInstance(Review.place_id, str)

    def test_name_user_id_type(self):
        self.assertIsInstance(Review.user_id, str)

    def test_name_text_type(self):
        self.assertIsInstance(Review.text, str)


class TestReview_inherit(unittest.TestCase):
    '''Unittests for Review inheritance'''

    def test_classname_in_str(self):
        self.assertIn('Review', Review().__str__())

    def test_id_in_str(self):
        self.assertIn('id', Review().__str__())

    def test_dict_method(self):
        self.assertIsInstance(Review().__dict__, dict)

    def test_no_args_init(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_str(self):
        self.assertIsInstance(Review().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(Review().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(Review().updated_at, datetime)

    def test_different_id(self):
        rat1 = Review()
        rat2 = Review()
        self.assertNotEqual(rat1.id, rat2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        um = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(um.id, "345")
        self.assertEqual(um.created_at, dt)
        self.assertEqual(um.updated_at, dt)

    def test_one_save(self):
        um = Review()
        sleep(0.05)
        first_updated_at = um.updated_at
        um.save()
        self.assertIsInstance(first_updated_at, datetime)
        self.assertNotEqual(type(um.updated_at), str)

    def test_save_with_arg(self):
        um = Review()
        with self.assertRaises(TypeError):
            um.save(None)
            self.assertIn(umid, f.read())

    def test_to_dict_type(self):
        um = Review()
        self.assertIsInstance(um.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        um = Review()
        um_dict = um.to_dict()
        self.assertEqual(str, type(um_dict["created_at"]))
        self.assertEqual(str, type(um_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        um = Review()
        um.id = "123456"
        um.created_at = um.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(um.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
