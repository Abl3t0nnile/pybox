import urwid
from urwid.container import Columns, Frame

from .widgets import StoryBoard, SideBar


class GameView(Frame):
    
    
    _story = StoryBoard()
    _side = SideBar()
    _input = None
    
    _body = Columns([
        ('weight', 6, _story),
        ('weight', 4, _side),
    ])
    
    def __init__(self, application) -> None:
        self._application = application
        super(GameView, self).__init__(self._body, footer=self._input)
    
    @property
    def storyPanel(self):
        return self._story
    @property
    def sideBar(self):
        return self._side
    @property
    def inputField(self): pass
    
    def update_story(self): pass
    def update_locTab(self, mode: str, obj: object):
        self._side.update_location(mode, obj)
    def update(self): pass

class MainMenuView: pass

class HelpView: pass