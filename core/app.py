from .session import Session
from ..database import PyBoxDB
from ..tools import load_json
from ..ui import SimpleInterface

from urwid import MainLoop

import os

class PyBoxApplication:
    
    def __init__(self, uiClass=SimpleInterface):
        self.__path = os.getcwd()
        self.__data = self.__path + '/data/'
        self.session = Session
        self.db = PyBoxDB(self.__path)
        self.uiClass = uiClass
    
    def init(self, session=None):
        if not session:
            self.session = Session(self.db.scenes['libSeats'])
        else:
            self.session = session
        self.ui = self.uiClass(self)
    
    def _get__dataPath(self) -> str:
        return self.__data
    data = property(_get__dataPath)
    
    def handle_userInput(self, request: str):
        self.ui.update_storyPanel(request)
    
    def move_player(self, direction):
        try:
            msg = self.session.set_next_scene(direction)
        except AssertionError as error:
            msg = str(error)
        finally:
            self.ui.update_storyPanel(msg)
            self.ui.update_storyTitle(self.session.scene.name)
        
        if self.session.scene.visited:
            pass
        else:
            self.look_around()
            self.session.scene.visited = True
            self.db.commit()
        
        self.ui.focus_lastStoryEntry()
    
    def look_around(self):
        textFile = load_json(self.data+'text_scenes.json')
        msg = textFile[self.session.scene.alias]['description']
        self.ui.update_storyPanel(msg)
    
    def run(self):
        MainLoop(self.ui).run()