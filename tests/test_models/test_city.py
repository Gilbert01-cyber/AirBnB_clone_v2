#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        """Test that a new instance is a City."""
        city = City()
        self.assertIsInstance(city, City)

    def test_inherits_base_model(self):
        """Test that City inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_state_id_is_string(self):
        """Test that state_id attribute is a string."""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_name_is_string(self):
        """Test that name attribute is a string."""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        city = City()
        self.assertEqual(city.to_dict()["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
