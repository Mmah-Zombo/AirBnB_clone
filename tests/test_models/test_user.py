#!/usr/bin/python3
"""Unittests for the User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittesting for the User class"""

    def setUp(self):
        """Set up test fixtures"""
        self.user = User()

    def test_attribute_default_values(self):
        """Test User attribute default values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_email_attribute(self):
        """Test User email attribute"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Test User password attribute"""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Test User first_name attribute"""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Test User last_name attribute"""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_str_representation(self):
        """Test the __str__ method"""
        user_str = str(self.user)
        class_name = self.user.__class__.__name__
        expected_str = "[{}] ({}) {}".format(class_name,
                                             self.user.id, self.user.__dict__)
        self.assertEqual(user_str, expected_str)


if __name__ == '__main__':
    unittest.main()
