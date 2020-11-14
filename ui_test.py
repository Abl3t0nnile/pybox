import urwid

class PyBoxWidget:
    "Die Basisklasse aller durch PyBox erweiterten :class:`urwid.Widgets <urwid.Widget>`."

class UserInterface: pass

class GameView():
    
    # --- Interfaceelemente
    # -------------------------------------------------------------------------
    # --- StoryPanel
    # ---  + --- Story Blocks (Aktionseingabe / Programmantwort)
    # ---  + --- Input Field
    # --- InfoPanel
    # ---  + --- Titel - I.d.R. Name des aktuellen Orts
    # ---  + --- Compass - Liste der möglichen Ausgänge
    # ---  + --- DataTile
    # ---         + --- Clock - Aktuelle Uhrzeit
    # ---         + --- Turns - Aktueller Spielzug
    # ---  + --- TabPanel - Durschaltbare Anzeige
    # ---         + --- LocTab - Zeigt Gegenstandsliste des aktuellen Raums
    # ---         + --- InvTab - Statusanzeige Spielrinventar
    # ---         + --- MenTab - Quick Menü für load / save, usw.

    def __init__(self, session):
        # Interface zu Laufzeitdaten, welche im Interface angezeigt werden
        self.__session = session
        # Subkomponenten des Interfaces
        self._inputField = None
        self._infoTitle = None
        self._dataTile = None
        self._compass = None
        self._locTab = None
        self._invTab = None
        self._menuTab = None