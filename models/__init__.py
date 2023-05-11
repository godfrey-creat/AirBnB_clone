#!/usr/bin/python3

"""The __init__ method for models """

from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
