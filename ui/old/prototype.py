import urwid

from pybox.core import Session
from pybox.game_objects import GameLocation


from urwid.container import Columns, Pile
from urwid.widget import Text

class UserInterface:
    
    def __init__(self, app) -> None:
        """Diese Klasse bietet den höchsten Abstraktionsgrad bei der Verwendung des PyBox User Interfaces. Sie bietet ein voll Funktionsfähiges textbasiertes User Interface auf Basis der `urwid` Bibliothek. Das Interface benötigt die PyBoxApplikation als Parameter.
        
            >>> from pybox.ui import UserInterface
            >>> gui = UserInterface(PyBoxApplication)
            >>> gui.run()
        """
        pass
    
    def run(self): pass

"""Das PyBox Interface ist ein zwei Hauptbestandteile unterteilt. Das :class:`StoryPanel` und :class:`InfoPanel`.

Das StoryPanel ist eine scrollbare Liste, welche die letzten 20 Befehlseingaben des Spielers und die daraus resultierenden Textanworten des Programms enthält. In der obersten Zeile wird der Name des Raums angezeigt, in dem sich der Spieler aktuell befindet. Bei fokussiertem StoryPanel wird in der letzten Zeile ein Eingabefeld erzeugt und fokussiert. Hier kann der Spieler ein weiteren Befehl eintippen.

Das InfoPanel bietet dem Spieler eine umfassende Übersicht wichtiger Informationen über die Spielwelt. Das InfoPanel ist in mehrere Bereiche unterteilt, wodurch die Informationen klar strukturiert dargestellt werden können.
An oberster stelle steht der Name des Raums, in dem sich der Spieler zum aktuellen Zeitpunkt befindet. Darunter werden die möglichen Ausgänge, die aktuelle InGame Zeit, sowie die Zahl der bisherigen Züge angezeigt.
Unter diesen Basisanzeigen folgt das TabPanel, bei dem es sich um ein durchschaltbares Interfaceelement handelt, das verschiedene Informationen anzeigen kann. Am Oberen Rand des Panels befinden sich Knöpfe mit denen sich die aktuelle Ansicht umschalten lässt. Darunter folgt der aktuell ausgewählte Tab.
Der InventoryTab gibt Auskunft über den Platz, sowie das Gewicht des Inventars und zeigt eine Liste der Gegenstände die sich aktuell im Spielerinventar befinden.
Der LocationTab zeigt eine Liste aller interaktiven Gegenstände in der Umgebung des Spielers an.
Der MenuTab ist eine Liste verschiedener Optionen wie z.B. Load/Save, Exit, usw.
"""

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

# --- StoryPanel und Elemente -------------------------------------------------

class StoryItem():

    def __init__(self) -> None:
        """
        """

class InputField():

    def __init__(self) -> None:
        """
        """

class StoryPanel():

    def __init__(self) -> None:
        """
        """

    

# --- InfoPanel und Elemente --------------------------------------------------

class TitlePrompt(PyBoxWidget):

    def __init__(self, currLoc, text=None) -> None:
        """
        """

        super(TitlePrompt, self).__init__('title')

        self._currLoc = currLoc
        self._widget = urwid.Text(u"Title Prompt", align='center')

        if not text:
            self.update()
        else:
            self.update(text)

    
    def update(self, text=None):
        if not text:
            content = self._currLoc
        else:
            content = text
        
        self._widget.set_text(u" {} ".format(content))

class Compass(PyBoxWidget):
    
    symbols = {
        'north': u"N",
        'south': u"S",
        'west': u"W",
        'east': u"E",
        'up': u"▲",
        'down': u"▼",
    }

    def __init__(self, loc) -> None:
        """
        """
        super(Compass, self).__init__('compass')
        
        self._currLoc = loc
        self._exits = urwid.Columns(self.build_exitList(loc))
        self._widget = urwid.Pile([
            urwid.Padding(urwid.Text(u"Kompass", align='center'), left=2, right=2),
            urwid.Padding(_line, left=2, right=2),
            urwid.Padding(urwid.Columns(
                self._exits
            ), left=2, right=2)
        ])
    
    def build_exitList(self, loc):
        
        extList = []
        for ext in loc.exits.keys():
            extList.append(urwid.Text(self.symbols[ext], align='center'))
            extList.append(urwid.Text(u"|", align='center'))
        
        if len(extList) > 0:
            extList.pop()
        
        print(extList)
        
        return extList
    
    def update(self, loc: object):
        
        self._exits.contents = self.build_exitList(self._currLoc)

class InfoTile(PyBoxWidget):

    def __init__(self, session) -> None:
        """
        """
        super(InfoTile, self).__init__('infoTile')
        
        self._time = session.clock
        self._turn = session.turn
        
        self.timeDisplay = urwid.Text(u"{}".format(self._time), align='center')
        self.turnDisplay = urwid.Text(u"{}".format(self._turn), align='center')
        
        self._widget = urwid.Pile([
            urwid. Columns([
                urwid.Text(u"Uhrzeit", align='center'),
                urwid.Text(u"Zug", align='center'),
            ]),
           _line,
            urwid. Columns([
                self.timeDisplay,
                self.turnDisplay,
            ]),
        ])
    
    def update(self):
        self.timeDisplay.set_text(u"{}".format(self._time))
        self.turnDisplay.set_text(u"{}".format(self._turn))

class InventoryTab():

    def __init__(self) -> None:
        """
        """

class LocationTab():

    def __init__(self) -> None:
        """
        """

class MenuTab():

    def __init__(self) -> None:
        """
        """

class TabPanel():

    def __init__(self) -> None:
        """
        """

class InfoPanel(PyBoxWidget):

    def __init__(self, components = []) -> None:
        """
        """
        super(InfoPanel, self).__init__('infoPanel')
        
        widgetList = [_blank]
        
        for component in components:
            widgetList.append(component.widget)
            widgetList.append(_blank)
        
        self._widget = urwid.Filler(urwid.Padding(
            urwid.Pile(widgetList), left=2, right=2), 'top')

# --- GameView ----------------------------------------------------------------

class GameView():

    def __init__(self, session) -> None:
        """Der GameView stellt die interaktive Benutzeroberfläche innerhalb einer aktiven Spielsession dar. Er benötigt die aktuelle :class:`Session` als Attribut, um aus dieser alle dargestellten Informationen abzuleiten.
        """
        self.session = session
        
        # --- UI Sub Components -----------------------------------------------
        
        self.inputFiled = InputField()
        self.titlePrompt = TitlePrompt(session.currentLoc)
        self.compass = Compass(session.currentLoc)
        self.infoTile = InfoTile(self.session.turn, self.session.clock)
        self.menuTab = MenuTab()
        self.locTab = LocationTab(self.session.currentLoc)
        self.invTab = InventoryTab(self.session.player)
        self.tabPanel = TabPanel(self.locTab, self.invTab, self.menuTab)
        
        # --- UI Main Components ----------------------------------------------
        
        self.stoyPanel = StoryPanel(self.inputFiled)
        
        infoContentList = [
            self.titlePrompt,
            self.compass,
            self.infoTile,
            self.tabPanel
        ]
        
        self.infoPanel = InfoPanel(infoContentList)
    
    
    def submit_userInput(self) -> str:
        "Gibt den aktuellen Inhalt aus und löscht das Eingabefeld."
        pass
    
    def refresh(self):
        "Rendert das Interface neu und aktualisiert alle angezeigten Parameter."
        pass
    
    def update_story(self, text: str):
        "Fügt dem StoryPanel einen neuen Eintrag hinzu."
        pass

if __name__ == "__main__":
    
    palette = [
        ('title', 'black,bold', 'white'),
        ('compass', 'black', 'light gray'),
        ('infoTile', 'black', 'light gray'),
        ('infoPanel', 'black', 'dark gray'),
    ]
    
    
    loc = GameLocation('roomA', 'Testkammer', {"north": u"Test", "up": u"Test2"})
    
    session = Session()
    session.currLoc = loc

    t = TitlePrompt(loc)
    c = Compass(loc)
    i = InfoTile(session)
    
    panel = InfoPanel([t,c,i])

    urwid.MainLoop(urwid.Frame(panel.widget), palette=palette).run()