#!/usr/bin/python3
"""Unittests for the file storage"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = 'file.json'
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all method of FileStorage."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

        # Add a new object and check if it's present in the storage
        obj = BaseModel()
        self.storage.new(obj)
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

    def test_save(self):
        """Test the save method of FileStorage."""
        # Add a new object and save it
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Check if the file was created and contains the object
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as file:
            data = file.read()
            self.assertIn(f"BaseModel.{obj.id}", data)
            self.assertIn('"__class__": "BaseModel"', data)
            self.assertIn('"id":', data)

    def test_reload(self):
        """Test the reload method of FileStorage."""
        # Save initial data
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Create a new FileStorage instance to reload from the file
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)
        self.assertIn(f"BaseModel.{obj2.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{obj1.id}"], obj1)
        self.assertEqual(all_objects[f"BaseModel.{obj2.id}"], obj2)

    def test_reload_empty_file(self):
        """Test the reload method when the JSON file is empty."""
        # Create an empty file
        with open(self.file_path, 'w') as file:
            file.write('')

        # Create a new FileStorage instance and reload from the empty file
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertEqual(all_objects, {})

    def test_reload_non_existent_file(self):
        """Test the reload method when the JSON file does not exist."""
        # Remove the file if it exists
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Create a new FileStorage instance and reload from non-existent file
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertEqual(all_objects, {})


if __name__ == '__main__':
    unittest.main()
