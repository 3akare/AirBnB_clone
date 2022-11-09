#!/usr/bin/env python3
'''User Model Testing'''
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_attribute(unittest.TestCase):
    '''Unittests for User Model'''

    def test_hasattr_email(self):
        new = User()
        self.assertTrue('email' in dir(new))

    def test_hasattr_password(self):
        new = User()
        self.assertTrue('password' in dir(new))

    def test_hasattr_first_name(self):
        new = User()
        self.assertTrue('first_name' in dir(new))

    def test_hasattr_last_name(self):
        new = User()
        self.assertTrue('last_name' in dir(new))

    def test_email_type(self):
        self.assertIsInstance(User.email, str)

    def test_first_name_type(self):
        self.assertIsInstance(User.first_name, str)

    def test_last_name_type(self):
        self.assertIsInstance(User.last_name, str)

    def test_password_type(self):
        self.assertIsInstance(User.password, str)


class TestUser_inherit(unittest.TestCase):
    '''Unittests for User inheritance'''

    def test_classname_in_str(self):
        self.assertIn('User', User().__str__())

    def test_id_in_str(self):
        self.assertIn('id', User().__str__())

    def test_dict_method(self):
        self.assertIsInstance(User().__dict__, dict)

    def test_no_args_init(self):
        self.assertEqual(User, type(User()))

    def test_id_is_str(self):
        self.assertIsInstance(User().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(User().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(User().updated_at, datetime)

    def test_different_id(self):
        rat1 = User()
        rat2 = User()
        self.assertNotEqual(rat1.id, rat2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        um = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(um.id, "345")
        self.assertEqual(um.created_at, dt)
        self.assertEqual(um.updated_at, dt)

    def test_one_save(self):
        um = User()
        sleep(0.05)
        first_updated_at = um.updated_at
        um.save()
        self.assertIsInstance(first_updated_at, datetime)
        self.assertNotEqual(type(um.updated_at), str)

    def test_save_with_arg(self):
        um = User()
        with self.assertRaises(TypeError):
            um.save(None)
            self.assertIn(umid, f.read())

    def test_to_dict_type(self):
        um = User()
        self.assertIsInstance(um.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        um = User()
        um_dict = um.to_dict()
        self.assertEqual(str, type(um_dict["created_at"]))
        self.assertEqual(str, type(um_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        um = User()
        um.id = "123456"
        um.created_at = um.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(um.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
