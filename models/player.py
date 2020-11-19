from persistent import Persistent
from persistent.list import PersistentList

class Player(Persistent):
    
    def __init__(self, initPos):
        # :class:`Scene`, in der sich der Spieler gerade befindet
        self.__position = initPos
        self.__inventory = PersistentList()
    
    def _get__position(self) -> Persistent:
        return self.__position
    position = property(_get__position)
    
    def _get__inventory(self) -> PersistentList:
        return self.__inventory
    inventory = property(_get__inventory)
    
    def move(self, direction: str):
        newPosition = self.__position.get_exit(direction)
        if not newPosition:
            pass
        else:
            self.__position = newPosition
            print(f'Du befindest Dich jetzt in: "{newPosition}"')