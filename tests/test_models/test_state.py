#!/usr/bin/env python3
'''State Model Testing'''
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_attribute(unittest.TestCase):
    '''Unittests for State Model'''

    def test_hasattr_name(self):
        new = State()
        self.assertTrue('name' in dir(new))

    def test_name_type(self):
        self.assertIsInstance(State.name, str)


class TestState_inherit(unittest.TestCase):
    '''Unittests for State inheritance'''

    def test_classname_in_str(self):
        self.assertIn('State', State().__str__())

    def test_id_in_str(self):
        self.assertIn('id', State().__str__())

    def test_dict_method(self):
        self.assertIsInstance(State().__dict__, dict)

    def test_no_args_init(self):
        self.assertEqual(State, type(State()))

    def test_id_is_str(self):
        self.assertIsInstance(State().id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_different_id(self):
        rat1 = State()
        rat2 = State()
        self.assertNotEqual(rat1.id, rat2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        um = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(um.id, "345")
        self.assertEqual(um.created_at, dt)
        self.assertEqual(um.updated_at, dt)

    def test_one_save(self):
        um = State()
        sleep(0.05)
        first_updated_at = um.updated_at
        um.save()
        self.assertIsInstance(first_updated_at, datetime)
        self.assertNotEqual(type(um.updated_at), str)

    def test_save_with_arg(self):
        um = State()
        with self.assertRaises(TypeError):
            um.save(None)

            self.assertIn(umid, f.read())

    def test_to_dict_type(self):
        um = State()
        self.assertIsInstance(um.to_dict(), dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        um = State()
        um_dict = um.to_dict()
        self.assertEqual(str, type(um_dict["created_at"]))
        self.assertEqual(str, type(um_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        um = State()
        um.id = "123456"
        um.created_at = um.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(um.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
