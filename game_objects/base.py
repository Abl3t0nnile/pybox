class _GameObject:
    
    def __init__(self, name: str, word: str, **kwargs) -> None:
        # Eindeutiger Identifikator dieser Instanz
        self.__id = id(self)
        # Bezeichner des Objekts, u.a. zur Referenz in Datenbanken
        self.__name = name
        # Substantiv für das Objekt, z.B. "Tisch"
        self.woordRoot = word.lower()
        # Erweiterung des Substantives, z.B. "Schreib"
        self.wordPrefix = None
        # Liste usätzliche Beschreibungen, z.B. ['antiker', 'großer']
        self.wordAdd = []
        # Initialisiert zusätzliche Attribute oder überschreibe Default
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @property
    def objId(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    
    def __str__(self) -> str:
        if not self.wordPrefix:
            word = self.woordRoot.capitalize()
        else:
            word = self.wordPrefix.capitalize() + self.woordRoot
        
        if len(self.wordAdd) == 0:
            return word
        else:
            return ", ".join(self.wordAdd) + ' ' + word

class _Location(_GameObject):
    
    def __init__(self, name: str, word: str, exits: dict, **kwargs) -> None:
        self._exits = exits
        self._content = []
        super(_Location, self).__init__(name, word, **kwargs)
    
    @property
    def exits(self) -> dict:
        return self._exits
    @property
    def exitPoints(self) -> list:
        return [key for key in self._exits]
    
    @property
    def assets(self) -> list:
        return self._content



