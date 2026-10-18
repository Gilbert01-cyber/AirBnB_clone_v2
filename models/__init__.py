#!/usr/bin/python3
"""Initialize the models package with a unique FileStorage instance."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
