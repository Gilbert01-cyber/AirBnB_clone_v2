#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance(self):
        """Test that a new instance is an Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_inherits_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_is_string(self):
        """Test that name attribute is a string."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_name_default_empty(self):
        """Test that name defaults to an empty string."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        amenity = Amenity()
        self.assertEqual(amenity.to_dict()["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()
