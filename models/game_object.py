from persistent import Persistent
from persistent.list import PersistentList
from persistent.mapping import PersistentMapping

class GameObject(Persistent):
    """Die Basisklasse aller Objekte, die in der Objektdatenbank eines PyBox Projekts gespeichert werden. Diese Basisklasse ist für In Game Objekte wie z.B. Szenen oder Assets vorgesehen.
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
        return self.__alias
    alias = property(_get__alias)
    
    def _get__name(self) -> str:
        "Read only Property, das eine Objektbezeichnung in Form eines Strings enthält."
        name = ''
        name += ', '.join(self.nameAdditions)
        if not self.namePrefix:
            name += self._name.capitalize()
        else:
            name += self.namePrefix.capitalize() + self._name
        return name
    name = property(_get__name)
    
    def __str__(self):
        return self.name