#!/usr/bin/python3
"""Unittests for the file storage"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before running the tests."""
        cls.file_path = 'file.json'
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test environment after running the tests."""
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def setUp(self):
        """Set up a clean environment for each test."""
        self.storage.reload()

    def test_all(self):
        """Test the all method of FileStorage."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

        # Add a new object and check if it's present in the storage
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{obj.id}"], obj)

    def test_new(self):
        """Test the new method of FileStorage."""
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{obj.id}"], obj)

    def test_save_reload(self):
        """Test the save and reload methods of FileStorage."""
        # Add a new object and save it
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Create a new FileStorage instance to reload from the file
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{obj.id}"], obj)

    def test_save_existing_file(self):
        """Test saving to an existing JSON file."""
        # Save initial data
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()

        # Create a new FileStorage instance to reload from the file
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{obj1.id}"], obj1)

        # Add a new object and save again
        obj2 = BaseModel()
        new_storage.new(obj2)
        new_storage.save()

        # Reload from the file and check if both objects are present
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)
        self.assertIn(f"BaseModel.{obj2.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{obj1.id}"], obj1)
        self.assertEqual(all_objects[f"BaseModel.{obj2.id}"], obj2)


if __name__ == '__main__':
    unittest.main()
