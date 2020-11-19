from persistent import Persistent
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList

from .game_object import GameObject

class _SceneConnection:
    """
    Eine Verbindung zwischen zwei Instanzen von :class:`Scene`.
    """
    def __init__(self, pointer, boundObj):
        # Pointer, der auf die verbundene Szene zeigt
        self.__pointer = pointer
        # Objekt, das als "Tür" fungiert. Default ist None.
        self.__boundObj = boundObj
    
    def _get_pointer(self) -> object:
        if not self.__boundObj:
            pass
        else:
            try:
                assert self.__boundObj.isOpen, f"Hier geht es nicht lang. {self.__boundObj} ist verschlossen."
            except AttributeError:
                pass
        return self.__pointer
    pointer = property(_get_pointer)
    
    def _get__boundObj(self) -> object:
        return self.__boundObj
    boundObj = property(_get__boundObj)

class Scene(GameObject):
    """
    Szenen bilden die Grundlage der Datenstruktur jedes PyBox Projekts.
    
    Eine Szene bilded den Interaktionshorizont ab, der dem Spieler innerhalb eines Zuges zur Verfügung steht. Das bedeutet, dass der Spieler mit allen Objekten, die sich in der aktuellen Szene befinden interagieren kann, ohne sich bewegen zu müssen.
    
    Der Spieler kann die aktuelle Szene wechseln, in dem er durch Bewegung einen der Ausgänge addressiert.
    """
    def __init__(self, alias: str, name: str):
        self.__exits = PersistentMapping()
        self.__assets = PersistentList()
        super(Scene, self).__init__(alias, name)
    
    def _get__exits(self) -> dict:
        "Read only Property, der Zugriff auf die Ausgänge einer Szene gewährt."
        return self.__exits
    exits = property(_get__exits)
    
    def get_exit(self, adress: str, default=None) -> object:
        "Gibt den Ausgang für die gegebene `address` aus, sofern vorhanden. Anderfalls wird `default` ausgegeben."
        try:
            return self.__exits[adress].pointer
        except KeyError:
            print("In diese Richtung für kein Weg.")
        except AssertionError as e:
            print(e)
        return default
    
    def _get_assets(self) -> PersistentList:
        "Read / Write Property, welches Zugriff auf die in der Szene referenzierten In Game Items bietet."
        return self.__assets
    def _set_assets(self, items: list) -> None:
        self.__assets = PersistentList(items)
    def _del_assets(self) -> None:
        self.__assets = PersistentList()
    assets = property(_get_assets, _set_assets, _del_assets)
    
    def add_assets(self, *args):
        for asset in args:
            if not isinstance(asset, GameObject):
                raise TypeError
            else:
                self.__assets.append(asset)
    
    def set_connection(self, other: object, address: str, boundObj: object=None):
        if not type(other) == Scene:
            raise TypeError
        self.__exits[address] = _SceneConnection(other, boundObj)