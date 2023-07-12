#!/usr/bin/python3
"""Unnittests for models/base_model.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_Save(unittest.TestCase):
    """unittests for the save public method"""
    def test_save_one(self):
        """tests if the save method works for a normal case"""
        obj = BaseModel()
        sleep(0.05)
        first_update_time = obj.updated_at
        obj.save()
        self.assertLess(first_update_time, obj.updated_at)


if __name__ == "__main__":
    unittest.main()
