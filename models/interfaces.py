from persistent import Persistent
from persistent.list import PersistentList

_infinite_ = 0

class container(Persistent):
    """Container können andere persistente Objekte enthalten.
    
    Diese Klasse implementiert lediglich das `content` Interface. Für
    Container mit weiteren Funktionen, wie z.B. `open/close` gibt es eigene
    Templates.
    """
    def __init__(self) -> None:
        self.__content = PersistentList([])
        self.maxCapacity = _infinite_
    
    def __len__(self):
        return len(self.__content)
    def __contains__(self, item):
        for obj in self.__content:
            if obj == item or obj.alias == item:
                return True
        return False
    
    def _get__capacity(self) -> int:
        """Read only Property. Berechnet den verbleibenden Platz im Container
        und gibt den Wert als Integer aus. Bei unbegrenzten Containern ist der
        Wert immer 0."""
        if self.maxCapacity == _infinite_:
            return _infinite_
        else:
            return self.maxCapacity - len(self)
    capacity = property(_get__capacity)
    
    def _get__content(self) -> PersistentList:
        """Read / Write Property, welcher Zugriff auf den gesamten Inhalt des Containers gewährt. Enthält eine persistente Liste, deren maximale Größe über `container.maxCapacity` begrenzt werden kann."""
        return self.__content
    def _set__content(self, content: list) -> None:
        if self.maxCapacity and self.maxCapacity < len(content):
            raise ValueError('Content to large to fit in Container!')
        self.__content = PersistentList(content)
    def _del__content(self) -> None:
        self.__content = PersistentList([])
    content = property(_get__content, _set__content, _del__content)
    
    def show_content(self):
        title = str(self) + "- Inhalt"
        print(title)
        print('-'*len(title))
        print(', '.join([str(item) for item in self.__content]))
    def add_item(self, item):
        # Überprüft, ob item ein persistentes Objekt ist
        if not isinstance(item, Persistent):
            raise TypeError
        # Überprüft, ob genug Platz im Container ist
        if not self.maxCapacity:
            pass
        else:
            assert self.capacity, "{item} passt nicht mehr in {container}"
        # Fügt das Objekt zum Container hinzu
        self.__content.append(item)
    def fetch_item(self, alias) -> Persistent:
        """Entfernt das Item mit dem gegeben `alias` aus dem Container und gibt es aus. Andernfalls wird ein AssertionError erzeugt.
        """
        # Durchsucht den Container nach einem Item mit gegebenem alias
        item_found = False
        for index, obj in enumerate(self.__content):
            if obj.alias == alias:
                item_found = True
                break
        # prüfe ob das Objekt im Container ist und gibt einen entsprechenden
        # Fehlerbericht aus
        assert item_found, "{item} befindet sich nicht in {container}"
        
        return self.__content.pop(index)
