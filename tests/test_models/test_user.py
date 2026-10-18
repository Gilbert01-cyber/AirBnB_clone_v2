#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instance(self):
        """Test that a new instance is a User."""
        user = User()
        self.assertIsInstance(user, User)

    def test_inherits_base_model(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_email_is_string(self):
        """Test that email attribute is a string."""
        user = User()
        self.assertIsInstance(user.email, str)

    def test_password_is_string(self):
        """Test that password attribute is a string."""
        user = User()
        self.assertIsInstance(user.password, str)

    def test_first_name_is_string(self):
        """Test that first_name attribute is a string."""
        user = User()
        self.assertIsInstance(user.first_name, str)

    def test_last_name_is_string(self):
        """Test that last_name attribute is a string."""
        user = User()
        self.assertIsInstance(user.last_name, str)

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        user = User()
        self.assertEqual(user.to_dict()["__class__"], "User")


if __name__ == "__main__":
    unittest.main()
