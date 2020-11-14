"""
PyBox.Language
--------------

Doc String des Sprach Pakets.
"""

from tinydb import TinyDB, where

class SpeechPack:
    
    def __init__(self, path: str) -> None:
        self._data = TinyDB(path + "/data/speech_pack.json")