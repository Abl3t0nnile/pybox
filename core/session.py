from .player import Player
from persistent import Persistent

from ..models import Scene

class Session(Persistent):
    
    def __init__(self, initScene: Scene) -> None:
        self.__currentScene = initScene
        self.__player = Player(initScene)
    
    def _get__scene(self) -> Scene:
        return self.__currentScene
    def _set__scene(self, scene: Scene) -> None:
        if not isinstance(scene, Scene):
            raise TypeError
        else:
            self.__currentScene = scene
    scene = property(_get__scene, _set__scene)
    
    def _get__player(self) -> Player:
        return self.__player
    player = property(_get__player)
    
    def set_next_scene(self, direction: str) -> None:
        "Ändert `self.scene` basierend auf der gegebenen `direction`."
        
        nextScene = self.__currentScene.get_adjacent_scene(direction)
        
        assert nextScene, "In diese Richtung führt kein Weg."
        
        self.__currentScene = nextScene
        self.__player.position = nextScene
        
        directions = {
            'n':'Norden',
            's': 'Süden',
            'w': 'Westen',
            'e': 'Osten',
            'u': 'Oben',
            'd': 'Unten'}
        
        if direction in directions:
            message = f"Du gehst nach {directions[direction]}."
        else:
            message = ''
        
        return message