"""
PyBox.Ui
--------

Dieses Paket realisiert ein grafisches User Interface unter Verwendung der :mod:`urwid` Library::

    >>> from pybox.ui import UserInterface
    >>> ui = UserInterface(PyBoxApplication)
    >>> ui.run()

"""

from urwid.main_loop import MainLoop
from .views import GameView


class UserInterface(MainLoop):
    
    def __init__(self, application):
        self._gameView = GameView(application)
        super(UserInterface, self).__init__(self._gameView)
    
    def run(self):
        super(UserInterface, self).run()