"""Dieses Modul implementiert eine Reihe von Interface Widgets, auf Basis der `urwid` Library. Diese funktionalen Bausteine können zur Konstruktion benutzerdefiniert Menüs verwendet werden.
"""

from urwid.container import Columns, Frame, Overlay, Pile
from urwid.decoration import AttrMap, BoxAdapter, Filler, Padding
from urwid.graphics import LineBox
from urwid.listbox import ListBox, SimpleListWalker
from urwid.widget import Divider, Edit, SolidFill, Text
from urwid.wimp import Button

_blank = Divider()
_line = Divider(u"-")

class StoryBoard(ListBox): pass
class TabPanel(Pile): pass
class Tab(Pile):

    def __init__(self, title):
        self._header = [
            Text(u"{}".format(title))
        ]
        super(Tab, self).__init__()

class InfoTile(Pile): pass
class Compass(Pile): pass

class SideBar(Pile):
    
    compass = Compass()
    info = InfoTile()
    tabs = TabPanel()
    
    
    def __init__(self) -> None:
        super(SideBar, self).__init__([self.compass, self.info, self.tabs])
    
    def update_locTab(self): pass
    def update_invTab(self): pass
