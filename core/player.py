from ..core.types import SizedList
    

class Player:
    
    # Max. Anzahl getragener Gegenstände
    _inventorySize = 20
    # Max. Traglast
    _carryLoad = 10
    
    def __init__(self):
        self._inventory = SizedList(self._inventorySize)
    
    def _set_inventory(self, item):
        if not isinstance(item, list):
            raise TypeError
        else:
            self._inventor = SizedList(self._inventorySize, item)
    def _get_inventory(self):
        return self._inventory
    def _del_inventory(self):
        self._inventory = SizedList(self._inventorySize)
    
    inv = property(_get_inventory, _set_inventory, _del_inventory, doc="...")