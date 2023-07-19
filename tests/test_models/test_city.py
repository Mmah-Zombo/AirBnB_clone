#!/usr/bin/python3
"""Unittests for the City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unittesting for the City class"""

    def test_attribute_default_values(self):
        """Test City attribute default values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
