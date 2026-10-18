#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance(self):
        """Test that a new instance is a BaseModel."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_two_ids_are_different(self):
        """Test that two instances have different ids."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_is_dict(self):
        """Test that to_dict() returns a dictionary."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.to_dict(), dict)

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        my_model = BaseModel()
        self.assertEqual(my_model.to_dict()["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
