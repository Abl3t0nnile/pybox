"""Dieses Modul implementiert eine Auswahl an vorgefertigten Subklassen von :class:`pybox.models.GameObject`. Diese Templates definieren Interfaces für die jeweiligen Standardaktionen, die zur Verwendung mit dem entsprechenden Objekt vorgesehen sind.
"""

from persistent import Persistent
from persistent.list import PersistentList

from . import GameObject
from .interfaces import container

class SimpleContainer(GameObject, container):
    
    def __init__(self, alias: str, name:str) -> None:
        GameObject.__init__(self, alias, name)
        container.__init__(self)

class ClosedContainer(SimpleContainer):
    """Eine Erweiterung des Standardcontainers.
    
    Diese Klasse implementiert das `content`und das `open/close` Interface.
    """
    
    def __init__(self, alias: str, name: str) -> None:
        self.isOpague = True
        self.isOpen = False
        self.isLocked = False
        self.key = None
        super().__init__(alias, name)
    
    def show_content(self):
        assert (self.isOpen or not self.isOpague), "Das geht nicht! {container} ist geschlossen."
        self.__content.show_content()
    
    def add_item(self, item):
        assert self.isOpen, "Das geht nicht! {container} ist geschlossen."
        self.__content.add_item(item)
    def fetch_item(self, alias) -> GameObject:
        assert self.isOpen, "Das geht nicht! {container} ist geschlossen."
        self.__content.fetch_item()
    
    def opn(self) -> str:
        assert (not self.isLocked), "Das geht nicht! {container} ist verschlossen."
        assert (not self.isOpen), "{container} ist bereits geöffnet."
        self.isOpen = True
        return f"{self} is nun offen."
    def cls(self) -> str:
        assert self.isOpen, "{container} ist bereits geschlossen."
        self.isOpen = False
        return f"{self} ist nun geschlossen."
    def lock(self, key):
        assert self.key, "{container} lässt sich nicht verschließen."
        assert (not self.isLocked), "{container} ist bereits verschlossen."
        assert (self.key == key), "{key} ist nicht der richtige Schlüssel für {container}."
        self.isLocked = True
        print(f"{self} ist nun verschlossen.")
    def unlock(self, key):
        assert self.key, "{container} lässt sich nicht aufschließen oder entriegeln."
        assert self.isLocked, "{container} ist bereits entriegelt."
        assert self.key == key, "{key} ist nicht der richtige Schlüssel für {container}."
        self.isLocked = True
        print(f"{self} ist nun entriegelt.")

class Surface(GameObject):
    
    def __init__(self, alias: str, name: str) -> None:
        self.__surface = container()
        self.isSeat = False
        self.isBed = False
        super().__init__(alias, name)
    
    def _get__surface(self) -> container:
        return self.__surface
    def _set__surface(self, content: list) -> None:
        self.__surface.content = content
    def _del__surfac(self) -> None:
        del self.__surface.content