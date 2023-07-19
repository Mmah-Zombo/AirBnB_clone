#!/usr/bin/python3
"""Unittests for the State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittesting for the State class"""

    def test_attribute_default_values(self):
        """Test State attribute default values"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
