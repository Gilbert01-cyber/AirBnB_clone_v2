#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_instance(self):
        """Test that storage is a FileStorage instance."""
        self.assertIsInstance(storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        my_model = BaseModel()
        storage.new(my_model)
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test that save() creates the file.json."""
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        with open("file.json", "r") as f:
            content = f.read()
            self.assertIn(my_model.id, content)


if __name__ == "__main__":
    unittest.main()
