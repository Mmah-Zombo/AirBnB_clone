#!/usr/bin/python3
"""Unittests for the BaseModel"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittesting for each method and attribute of the BaseModel"""
    def test_save_updates_updated_at(self):
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_to_dict_returns_dict_representation(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_id_is_string(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_created_at_is_datetime(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_str_representation(self):
        obj = BaseModel()
        obj_str = str(obj)
        class_name = obj.__class__.__name__
        expected_str = f"[{class_name}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(obj_str, expected_str)


if __name__ == '__main__':
    unittest.main()
