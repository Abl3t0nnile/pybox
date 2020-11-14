Das PyBox User Interface
========================
Obwohl es sich bei PyBox um ein Framework zum erstellen von Text Adventures handelt, bietet die Engine ein voll funktionsfähiges, grafisches User Interface. Zur Implementation dieses UI kommt das `urwid` Paket zum Einsatz. Somit lässt sich ein flexibles und interaktives Interfaces realisieren. PyBox setzt dabei auf eine kombinierte Nutzung von Maus und Tastatur zur Steuerung des Programms. Um den Implementationsaufwand gering zu halten, bietet die Engine eine Vorauswahl an Bildschirmen, welche für spezielle Anwendungsfälle optimiert sind und so eine optimale Schnittstelle zum Umgang mit der Engine bieten.

.. attention::

    Die eigentliche Laufzeitumgebung und das User Interface sind strikt von einander getrennt. Das UI stellt lediglich ausgewählte Daten der Laufzeitumgebung dar und gibt die Eingaben des Users an die PyBox Applikation weiter. Das UI selbst modifiziert **niemals** andere Komponenten der Laufzeitumgebung.

.. code-block:: python
    :name: class_ui
    :caption: User Interface Base Class

    class PyBoxUserInterface:

        def __init__(self, session) -> None:
            pass