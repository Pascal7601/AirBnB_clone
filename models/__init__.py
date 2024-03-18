#!/usr/bin/python3
"""
Script to instantiate a FileStorage object and reload data.

This script instantiates a FileStorage object from the file_storage module
and then reloads data from the file. It is typically used in conjunction with
other modules or scripts in a larger project that require data persistence.
"""

from models.engine.file_storage import FileStorage

# Instantiate a FileStorage object
storage = FileStorage()

# Reload data from the file
storage.reload()
