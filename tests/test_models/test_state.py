#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance(self):
        """Test that a new instance is a State."""
        state = State()
        self.assertIsInstance(state, State)

    def test_inherits_base_model(self):
        """Test that State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_name_is_string(self):
        """Test that name attribute is a string."""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_name_default_empty(self):
        """Test that name defaults to an empty string."""
        state = State()
        self.assertEqual(state.name, "")

    def test_to_dict_has_class_key(self):
        """Test that to_dict() includes the class name."""
        state = State()
        self.assertEqual(state.to_dict()["__class__"], "State")


if __name__ == "__main__":
    unittest.main()
