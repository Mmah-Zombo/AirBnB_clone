#!/usr/bin/python3
"""Unittests for the Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittesting for the Review class"""

    def test_attribute_default_values(self):
        """Test Review attribute default values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
