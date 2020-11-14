from ..core.types import Clock
from ..core.player import Player

class Session:
    
    def __init__(self) -> None:
        """Die Session bietet das Hauptinterface zu laufzeitrelevanten Daten. Sie ist für die Verwaltung der Aktuellen Sitzung zuständig und bietet die möglichkeit das Spiel zu speichern und zu laden.
        """
        self.currLoc = None
        self.player = Player
        self.turn = 0
        self.clock = Clock(8,0)
        # Zuletzt vom Spieler addressiertes Objekt
        self._focus = None
        # Alle Objekte mit denen der Spieler interagieren kann
        self.__focusList = []
    
    def init(self, **kwargs):
        "Initialisiert die Session und läd alle relevanten Parameter."
        pass
    
    def load_game(self, path): pass
    def save_game(self, path): pass
    
    def _get__focus(self):
        return self.__focus
    def _set__focus(self, value):
        raise Warning('Attribute Assignment not permitted, Session.focus is read only!')
    def _del__focus(self):
        raise Warning('Attribute Assignment not permitted, Session.focus is read only!')
    focus = property(_get__focus, _set__focus, _del__focus, "Ein read only Attribut, welches das Objekt ausgibt, was sich derzeit im Fokus befindet.")

    def update_focus(self):
        "Aktualisiert die Fokus Liste, basierend auf `curLoc` und `player.inv`."
        focusList = []
        if not self.curLoc:
            pass
        else:
            for item in self.currLoc.assets:
                focusList.append(item)
        
        for item in self.player.inv:
            focusList.append(item)
        
        self.__focusList = focusList
