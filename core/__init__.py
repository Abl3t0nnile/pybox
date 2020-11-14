"""
PyBox.Core
----------

Das Core Paket enthält Laufzeitumgebung der Engine. Hier laufen alle Bestandteile der Engine zusammen. Die :class:`PyBoxApplication` ist das top Level Objekt, dass jede Session verwaltet. Die :class:`Session` bietet dabei zugriff auf die laufzeitrelevanten Daten einer aktiven Sitzung.
"""

# from .application import PyBoxApplication
from .session import Session

