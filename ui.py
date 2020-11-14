
import urwid
from urwid.container import Columns
from urwid.widget import Text


_blank = urwid.Divider()
_line = urwid.Divider('-')

class PyBoxWidget:
    
    def __init__(self, styleClass='default') -> None:
        "Ein Wrapper um ein :class:`urwid.Widget` eines beliebigen Typs. Dient zur Verknüpfung eines bestimmten Interfaceelements mit weiteren Attributen und Methoden."
        self._widget = urwid.Widget
        self._styleClass = styleClass
    
    @property
    def widget(self) -> urwid.Widget:
        return urwid.AttrMap(self._widget, self._styleClass)
    
    def set_style(self, styleClass: str):
        self._styleClass = styleClass


class LocTab(PyBoxWidget):
    
    def __init__(self) -> None:
        super(LocTab, self).__init__('tab')
        self._widget = urwid.Pile([
            _blank,
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            urwid.Padding(urwid.Text(u"Test"), left=2, right=2),
            _blank,
        ])

class TabPanel(PyBoxWidget):
    
    _titel = urwid.Text(u"- Tab Panel -", align='center')
    
    _currentTab = 0
    
    _tabs = []
    
    def __init__(self, tabs: list):
        super(TabPanel, self).__init__('tabPanel')
        
        for tab in tabs:
            self._tabs.append(tab.widget)
        
        self._widget = urwid.Pile([
            _blank,
            self._titel,
            urwid.Padding(_line, left=2, right=2),
            _blank,
            self._tabs[self._currentTab],
        ])


class InfoPanel(PyBoxWidget):
    
    _title = urwid.Text(u"Info Panel", align='center')
    _time = urwid.Text(u"00:00", align='center')
    _turn = urwid.Text(u"1", align='center')
    _exits = urwid.Columns([])
    
    _invTab = None
    _locTab = LocTab()
    _menTab = None
    
    _tabPanel = TabPanel([_locTab])
    
    _widgetList = [
        _blank,
        # --- Info Panel Title
        urwid.Padding(
            urwid.AttrWrap(urwid.Pile([
                _title,
                _line,
            ]), 'infoTitle'),
        left=4, right=4),
        _blank,
        # --- Info Tile
        urwid.Padding(
            urwid.AttrWrap(urwid.Pile([
                _blank,
                urwid.Pile([
                    urwid.Columns([
                        urwid.Text(u"Uhrzeit", align='center'),
                        urwid.Text(u"Zug", align='center'),
                    ]),
                    urwid.Padding(_line, left=2, right=2),
                    urwid.Columns([
                        _time,
                        _turn,
                    ]),
                ]),
                _blank]),
            'infoTile'),
        left=2, right=2),
        _blank,
        # --- Compass
        urwid.Text(u"Kompass", align='center'),
        urwid.Padding(_line, left=4, right=4),
        _blank,
        urwid.Padding(
            urwid.AttrWrap(urwid.Pile([
                _blank,
                _exits,
                _blank,
            ]), 'compass'),
            left=2, right=2),
        urwid.Padding(
            _tabPanel.widget,
            left=2, right=2),
        _blank,
        urwid.BoxAdapter(urwid.SolidFill(), 100),
    ]
    
    _drctns = {
        'north': u"N",
        'south': u"S",
        'west': u"W",
        'east': u"E",
        'up': u"↑",
        'down': u"↓",
    }
    
    def __init__(self) -> None:
        super(InfoPanel, self).__init__('infoPanel')
        self._widget = urwid.Pile(self._widgetList)
        
    
    def set_title(self, text: str):
        self._title.set_text(u"{}".format(text))
    def set_time(self, value: str):
        self._time.set_text(u"{}".format(value))
    def set_turn(self, value: int):
        self._turn.set_text(u"{}".format(value))
    def set_exits(self, value: dict):
        exitList = []
        for key in value.keys():
            entry = self._drctns[key]
            exitList.append((urwid.Text(u"{}".format(entry), align='center'), urwid.Columns.options()))
            exitList.append((urwid.Text(u"|", align='center'), urwid.Columns.options()))
        if len(exitList) > 0:
            exitList.pop()
        self._exits.contents = exitList

    def change_active_tab(self, tab): pass

_txt = u"Hallo. Ich bin ein kleiner Blindtext. Und zwar schon so lange ich denken kann. Es war nicht leicht zu verstehen, was es bedeutet, ein blinder Text zu sein: Man ergibt keinen Sinn. Wirklich keinen Sinn. Man wird zusammenhangslos eingeschoben und rumgedreht – und oftmals gar nicht erst gelesen. Aber bin ich allein deshalb ein schlechterer Text als andere? Na gut, ich werde nie in den Bestsellerlisten stehen. Aber andere Texte schaffen das auch nicht. Und darum stört es mich nicht besonders blind zu sein. Und sollten Sie diese Zeilen noch immer lesen, so habe ich als kleiner Blindtext etwas geschafft, wovon all die richtigen und wichtigen Texte meist nur träumen."

class StoryPanel(PyBoxWidget):
    
    _inputField = urwid.Edit()
    _inputBar = urwid.Columns([
        ('weight', 1,urwid.Text(u"> ")),
        ('weight', 100, _inputField),
        ], min_width=2)
    
    _storyCache = urwid.SimpleListWalker([
        urwid.Padding(urwid.Text(_txt), left=2),
        _blank,
        urwid.Text(u"> öffne schublade"),
        _blank,
        urwid.Padding(urwid.Text(u"Das funktioniert nicht. Die Schreibtischschublade ist verschlossen."), left=2),
        _blank,
        _inputBar,
        _blank,
    ])
    
    def __init__(self) -> None:
        super(StoryPanel, self).__init__('storyPanel')
        self._widget = urwid.Padding(
            urwid.ListBox(self._storyCache),
        left=0, right=2)
    
    def get_userInput(self) -> str:
        return self._inputField.get_edit_text()
    
    def clear_userInput(self):
        self._inputField.set_edit_text(u"")
    
    def mirror_userInput(self):

        mirror = urwid.Text(u"> {}".format(self.get_userInput()))
        
        self._storyCache.insert(-2, mirror)
        self._storyCache.insert(-2, _blank)
    
    def add_storyPoint(self, text):
        
        reply = urwid.Padding(urwid.Text(u"{}".format(text)), left=2)
        self._storyCache.insert(-2, reply)
        self._storyCache.insert(-2, _blank)
        
        self._widget.original_widget.focus_position = len(self._storyCache) - 2

if __name__ == "__main__":
    
    def on_enter(key):
        if key == 'enter':
            storyPanel.mirror_userInput()
            storyPanel.add_storyPoint(u"Das ist eine Antwort auf Deine Eingabe: '{}'.".format(storyPanel.get_userInput()))
            storyPanel.clear_userInput()
        elif key == 'z':
            infoPanel.set_time('12:39')
        elif key == 't':
            infoPanel.set_turn(17)
        elif key == 'e':
            infoPanel.set_exits({'north': None, 'south': None, 'east': None, 'down': None})
        elif key == 'esc':
            raise urwid.ExitMainLoop
        
    
    palette = [
        ('storyPanel', '', ''),
        ('infoPanel', 'black', 'dark gray'),
        ('tabPanel', 'black', 'dark gray'),
        ('infoTitle', 'black', 'dark gray'),
        ('infoTile', 'black', 'light gray'),
        ('compass', 'black', 'light gray'),
        ('tab', 'black', 'light gray'),
    ]
    
    infoPanel = InfoPanel()
    infoPanel.set_exits({'north': None, 'west': None, 'up': None})
    
    storyPanel = StoryPanel()
    
    body = urwid.Columns([
        ('weight', 6, storyPanel.widget),
        ('weight', 4, urwid.Filler(infoPanel.widget, 'top')),
    ])
    
    frame = urwid.Frame(body)
    
    urwid.MainLoop(frame, palette, unhandled_input=on_enter).run()
