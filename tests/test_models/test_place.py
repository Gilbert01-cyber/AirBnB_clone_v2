#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance(self):
        """Test that a new instance is a Place."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_inherits_base_model(self):
        """Test that Place inherits from BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_city_id_is_string(self):
        """Test that city_id attribute is a string."""
        place = Place()
        self.assertIsInstance(place.city_id, str)

    def test_number_rooms_is_int(self):
        """Test that number_rooms attribute is an integer."""
        place = Place()
        self.assertIsInstance(place.number_rooms, int)

    def test_price_by_night_is_int(self):
        """Test that price_by_night attribute is an integer."""
        place = Place()
        self.assertIsInstance(place.price_by_night, int)

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        place = Place()
        self.assertEqual(place.to_dict()["__class__"], "Place")


if __name__ == "__main__":
    unittest.main()
