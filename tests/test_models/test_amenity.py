#!/usr/bin/python3
"""Unittests for the Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittesting for the Amenity class"""

    def test_attribute_default_values(self):
        """Test Amenity attribute default values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
