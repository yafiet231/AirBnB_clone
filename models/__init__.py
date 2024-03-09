#!/usr/bin/python3
"""__init__ method for models directory that assign storage
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
