from persistent import Persistent
from persistent.list import PersistentList
from persistent.mapping import PersistentMapping

class GameObject(Persistent):
    """Die Basisklasse aller interaktiven Spielobjekte.
    
    Implementiert das Standardinterface der PyBox Engine, sowie das Interface für persistente Objekte, die zur Verwendung mit einer :class:`ZODB` Datenbank vorgesehen sind.
    """
    def __init__(self, alias: str, name: str):
        # Identifiziert einen Gegenstand, nicht aber die Instanz eines Objekts
        # In einem Haufen aus 100 Goldmünzen, haben alle 100 Instanzen den
        # gleichen alias, sofern es sich um 100 identische Münzen handelt.
        # Jede Münze hat allerdings eine andere unique object id
        self.__alias = alias
        # Basis Substantiv z.B. Tisch
        # Bei Deklinationen wird nur dieser Wortstamm beachtet
        self._name = name
        # Substantivergänzung z.B. Schreib(tisch)
        # Ist deklinationsunabhängig
        self.namePrefix = None
        # Liste mit Adjektiven
        self.nameAdditions = PersistentList()
    
    def _get__alias(self) -> str:
        "Read only Property zur eindeutigen Identifikation einer bestimmten Instanz dieses Typs."
        return self.__alias
    alias = property(_get__alias)
    
    def _get__name(self) -> str:
        "Read only Property, welches eine Objektbezeichnung in Form eines Strings enthält."
        name = ''
        name += ', '.join(self.nameAdditions) + ' '
        if not self.namePrefix:
            name += self._name
        else:
            name += self.namePrefix + self._name
        return name.strip()
    name = property(_get__name)
    
    def __str__(self):
        return self.name
