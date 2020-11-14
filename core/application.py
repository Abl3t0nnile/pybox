import os

from .session import Session
from ..ui import UserInterface
from ..database import Database
from ..language import SpeechPack

class PyBoxApplication:
    """Das Herzstück jeder PyBox Anwendung. Dieses Objekt implementiert die grundlegende Programmstruktur und Funktionsweise der Engine. Es bietet Zugriff auf die aktive Programmsession, alle Projekt- und Sprachdaten, sowie das User Interface.
    
    Bei der Instanzierung wird automatisch der aktuelle Pfad ausgelesen und zur zum Auffinden weiterer Projektdaten verwendet.
    
    .. admonition:: Projektstruktur
    
        PyBox verwendet eine festgelegte Projektstruktur um das Auffinden verschiedener Daten zu erleichtern::
        
            project_folder/
             + --- data/
             |      + --- speech_pack.json
             |      + --- game_objects.json
             |      + --- text_book.json
             + --- save_games/
             + --- custom_scripts.py
             + --- game.py
    """
    def __init__(self, name: str):
        # Name des Projekts
        self.name = name
        # Pfad zu Projektdatein
        self.path = os.getcwd()
        # Die aktuelle Laufzeitsession
        self.__session = Session
        # Interface zur Objektdatenbank des Projects
        self.__objctDb = Database
        # Interface zur Sprachdatenbank des Projects
        self.__lngPck = SpeechPack
        # User Interface
        self.__ui = UserInterface
    
    
    def _get__session(self):
        return self.__session
    def _set__session(self):
        raise Warning('Value assignments on PyBoxApplication.session not supported!')
    def _del__session(self):
        raise Warning('Attribute deletion on PyBoxApplication.session not supported!')
    session = property(_get__session, _set__session, _del__session, "Ein read only Attribut, welches ein Interface zur aktiven Laufzeitsession bietet.")
    
    def _get__objctDb(self):
        return self.__objctDb
    def _set__objctDb(self):
        raise Warning('Value assignments on PyBoxApplication.objctDb not supported!')
    def _del__objctDb(self):
        raise Warning('Attribute deletion on PyBoxApplication.objctDb not supported!')
    objctDb = property(_get__objctDb, _set__objctDb, _del__objctDb, "Ein read only Attribut, welches ein Interface zur Projektdatenbank bietet.")
    
    def _get__lngPck(self):
        return self.__lngPck
    def _set__lngPck(self):
        raise Warning('Value assignments on PyBoxApplication.lngPck not supported!')
    def _del__lngPck(self):
        raise Warning('Attribute deletion on PyBoxApplication.lngPck not supported!')
    lngPck = property(_get__lngPck, _set__lngPck, _del__lngPck, "Ein read only Attribut, welches ein Interface zur Sprachdatenbank bietet.")
    
    
    def init(self, **kwargs):
        "Initialisiert grundlegende Attribute. Muss refereneziert werden, bevor die Applikation gestartet werden kann."
        self.__session.__init__(Session)
        self.__objctDb.__init__(Database, self.path)
        self.__lngPck.__init__(SpeechPack, self.path)
        self.__ui = UserInterface(self)
    
    def run(self):
        self.__ui.run()