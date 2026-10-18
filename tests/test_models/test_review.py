#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance(self):
        """Test that a new instance is a Review."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_inherits_base_model(self):
        """Test that Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_place_id_is_string(self):
        """Test that place_id attribute is a string."""
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_user_id_is_string(self):
        """Test that user_id attribute is a string."""
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_text_is_string(self):
        """Test that text attribute is a string."""
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        review = Review()
        self.assertEqual(review.to_dict()["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
