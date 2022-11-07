#!/usr/bin/env python3
""" File Storage Testing """
import unittest
import models
import json
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_init(unittest.TestCase):
    """Unittests for FileStorage init"""

    def test_for_init(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_presence_of_file_path(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_reload_no_file(self):
        self.assertRaises(TypeError, models.storage.reload())

    def test_presence_of_objects(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())

    def test_save(self):
        bm = BaseModel()
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_reload(self):
        bm = BaseModel()
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)


if __name__ == '__main__':
    unittest.main()
