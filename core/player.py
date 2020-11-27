from ..models.scenes import Scene
from persistent import Persistent
from persistent.list import PersistentList

class Player(Persistent):
    """Das Player Objekt repräsentiert den Avatar des Spielers in der Spielwelt. Da der Avatar in PyBox selbst Teil von Interaktionen sein kann, ist dieses Objekt persistent und wird somit in der Datenbank gespeichert."""
    def __init__(self, initPos: object):
        self.__position = initPos
        self.__inventory = PersistentList()
    
    def _get__position(self) -> object:
        """Read only Property, gewährt Zugriff die aktuelle Position des
        Spielers. Enthält eine :class:`Scene` Instanz, welche als
        Ausgangspunkt in der Objekthierarchie der Datenbank dient."""
        return self.__position
    def _set__position(self, s: Scene) -> None:
        if not isinstance(s, Scene):
            raise TypeError
        self.__position = s
    position = property(_get__position, _set__position)
    
    def _get__inventory(self) -> PersistentList:
        """Read only Property, enthält eine :class:`PersistentList`, welche
        alle Objekte im Spielerinventar enthält."""
        return self.__inventory
    inventory = property(_get__inventory)
