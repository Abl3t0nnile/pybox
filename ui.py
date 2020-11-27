"""
Dieses Modul enthält die einzelnen Widgets, aus denen die Interfaceelemente der PyBox Engine aufgebaut sind. Die Objekte dieses Moduls bieten ein auf PyBox abgestimmtes Interace zum :mod:`urwid` Paket.
"""


from urwid.main_loop import MainLoop
import urwid

from urwid import connect_signal
from urwid.container import Columns, Frame, Pile
from urwid.decoration import Filler, Padding
from urwid.graphics import LineBox
from urwid.listbox import ListBox, SimpleListWalker
from urwid.widget import Divider, Edit, Text
from urwid.wimp import Button

from pybox.session import Session

# --- TAGS --------------------------------------------------------------------

_bold_ = 'bold'
_emph_ = 'highlight'


# --- DESIGN ELEMENTS ---------------------------------------------------------

_blank = Divider()
_line = Divider(u"-")

# --- SUB COMPONENTS ----------------------------------------------------------

class Compass(LineBox):

    def __init__(self, exits: list) -> None:
        buttons = [Button(d) for d in exits]
        widget = Columns(buttons)
        super(Compass, self).__init__(widget)

class InfoTile(LineBox):

    def __init__(self, data: list) -> None:
        widget = Pile([
            Columns([
                Text(u"Uhrzeit", align='center'),
                Text(u"Zug", align='center')
            ]),
            _line,
            Columns([
                Text(u"12:39", align='center'),
                Text(u"17", align='center'),
            ])
        ])
        super(InfoTile, self).__init__(widget)

class LocationTab(Pile):
    
    _initContent = [
        Text(u"Gegenstände", align='center'),
        _line,
        _blank,
    ]
    
    def __init__(self):
        super(LocationTab, self).__init__(self._initContent)
    
    def clear(self) -> None:
        self.widget_list = self._initContent
    @property
    def content(self):
        return self.widget_list



class InventoryTab(Pile):

    _initContent = [
        Text(u"Inventar", align='center'),
        _line,
        _blank,
    ]
    
    def __init__(self):
        super(InventoryTab, self).__init__(self._initContent)

class MenuTab(Pile):

    _initContent = [
        Text(u"Menü", align='center'),
        _line,
        _blank,
        Button(u"Load"),
        Button(u"Save"),
        _blank,
        Button(u"Options"),
        Button(u"Help"),
        _blank,
        Button(u"Exit"),
    ]
    
    def __init__(self):
        super(MenuTab, self).__init__(self._initContent)

class NavBar(Columns):
    
    _locBtn = Button(u"[L]OC")
    _invBtn = Button(u"[I]NV")
    _menBtn = Button(u"[M]EN")
    
    def __init__(self) -> None:
        super(NavBar, self).__init__([
            self._locBtn,
            self._invBtn,
            self._menBtn,
        ])


class SideTab(LineBox):
    
    _navBar = NavBar()
    _locationTab = LocationTab()
    _inventoryTab = InventoryTab()
    _menuTab = MenuTab()
    
    _body = Pile([_navBar,  LineBox(_locationTab)])
    
    def __init__(self) -> None:
        connect_signal(self._navBar._locBtn, 'click', self.select_tab, "loc")
        connect_signal(self._navBar._invBtn, 'click', self.select_tab, "inv")
        connect_signal(self._navBar._menBtn, 'click', self.select_tab, "men")
        super(SideTab, self).__init__(self._body)


    @property
    def body(self):
        return self._body
    @property
    def invTab(self):
        return self._locationTab
    @property
    def locTab(self):
        return self._inventoryTab
    @property
    def menTab(self):
        return self._menuTab
    
    def select_tab(self, button, tab):
        if tab == 'loc':
            self._body.widget_list[1] = LineBox(self._locationTab)
        elif tab == 'inv':
            self._body.widget_list[1] = LineBox(self._inventoryTab)
        elif tab == 'men':
            self._body.widget_list[1] = LineBox(self._menuTab)
        else:
            pass


# --- UI COMPONENTS -----------------------------------------------------------

class StoryBoard(LineBox):
    """
    Dieses Fenster enthält den Großteil des Spieltextes. Hier werden die Aktionen des Spielers gespiegelt und die Antworten des Parsers ausgegeben. Das Fenster ist mit einem Rahmen umgeben ,der Titel gibt den aktuellen Aufenthaltsort des Spielers an.
    """
    
    _storyCacheSize = 40
    _storyCache = SimpleListWalker([_blank])
    _story = ListBox(_storyCache)
    
    def __init__(self) -> None:
        super(StoryBoard, self).__init__(self._story, title='Aktuelle Szene')

    def update_story(self, markup) -> None:
        "Fügt einen neuen Eintrag mit angeschlossener Leerzeile zum StoryBoard hinzu. Kürzt die Liste bei Bedarf, um nur die letzten X Einträge anzuzeigen."
        # Lösche die ersten beiden Einträge um Überlänge zu vermeiden
        if len(self._storyCache)>= self._storyCacheSize:
            self._storyCache.pop(0)
            self._storyCache.pop(0)
        # Füge neuen Eintrag und Leerzeile hinzu
        self._storyCache.append(Text(markup))
        self._storyCache.append(_blank)
        # Setze Fokus auf den neuesten Eintrag
        pos = len(self._storyCache) - 1
        self._story.set_focus(pos)
    
    def clear_story(self) -> None:
        "Löscht den gesamten Inhalt des StoryBoards."
        self._storyCache.clear()
        self._storyCache.append(_blank)


class SideBar(LineBox):
    
    _info = InfoTile([u"12:39", u"17"])
    _compass = Compass([u"N", u"W", u"▲"])
    _tabs = SideTab()

    
    _widgetList = [
        _blank,
        Text(u"Kompass", align='center'),
        _compass,
        _blank,
        Text(u"Info", align='center'),
        _info,
        _tabs,
    ]
    
    _widget = Pile(_widgetList)
    
    
    def __init__(self) -> None:
        super(SideBar, self).__init__(Filler(self._widget, 'top'))
    
    def switch_tab(self, tab) -> None: pass
    def update_compass(self, exits: list) -> None:
        self._compass = Compass(exits)
    def update_info(self, data: list) -> None:
        self._info = InfoTile(data)
    def update_location(self, data: dict) -> None: pass
    def update_inventory(self, data: dict) -> None: pass

class InputField(Columns): pass



class GameView(Frame):
    
    
    _story = StoryBoard()
    _side = SideBar()
    
    _body = Columns([
        ('weight', 6, _story),
        ('weight', 4, _side),
    ])
    
    def __init__(self, session: Session) -> None:
        self.session = session
        super(GameView, self).__init__(self._body)
    
    @property
    def storyPanel(self):
        return self._story
    @property
    def sideBar(self):
        return self._side
    @property
    def inputField(self): pass

    def update_title(self):
        self._story.set_title(u" {} ".format(self.session.scene.name))
