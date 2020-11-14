"""
PyBox.Database
--------------

Doc String des Datenbank Pakets.
"""

from tinydb import TinyDB, where

class Database:
    
    def __init__(self, path: str) -> None:
        self._gameObjects = TinyDB(path + "/data/game_objects.json")
        self._textBook = TinyDB(path + "/data/text_book.json")