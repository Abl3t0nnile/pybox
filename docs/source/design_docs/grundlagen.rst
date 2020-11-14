Grundlagen
==========

Jedes lauffähige Programm, welches die PyBox Engine verwendet, besteht aus einer Reihe fest Definierter Grundstrukturen.

Die interaktive Umgebung der PyBox Engine
-----------------------------------------

PyBox bietet.

PyBoxApplication
----------------

Die PyBoxApplication ist der oberste Layer von Abstraktion der Engine. Sie implementiert die Laufzeitumgebung und bietet ein Interface zu allen Subkomponenten der Engine. Eine Instanz dieses Objekts ist in der Lage einen gegebenen Projektdatensatz zu interpretieren und eine interaktive Session bereit zu stellen. Diese interaktive Session ermöglicht es dem Spieler sich frei in der Spielwelt zu Bewegen und unter Beachtung der Spielregeln mit dieser zu interagieren. Die Interaktion mit dem Programm wird über ein textbasiertes User Interface realisiert, welches durch die `urwid`_ Library implementiert ist.

.. _urwid: http://urwid.org/index.html

PyBoxMainLoop
-------------

Das Main Loop einer PyBox Applikation bietet eine vom Programmkern getrennte interaktive Oberfläche, welche über das User Interface gesteuert werden kann.

Standard Programmzyklus
-----------------------

Der Standard Programmzyklus bildet die Grundlage aller Interaktionsmöglichkeiten. Da PyBox auf eine grafische Benutzeroberfläche mit Auswahl- und Eingabeelementen setzt, ist der Standard Programmzyklus fest mit dem User Interface verknüpft. Zu Beginn jedes Zyklus kann der User entweder eine Texteingabe tätigen oder eines der Interfaceelemente Aktivieren. Dazu steht ihm entweder die Maus oder eine Reihe von Tastaturbefehlen zur Verfügung.

Befehlssatz
###########

* ENTER 
    - [fokussiertes Interface Element] - Aktivieren
    - [fokussiertes Eingabefeld] - Sendet die aktuelle Eingabe zur Interpretation an den Parser
* ESC 
    - Beendet das Programm nach Bestätigungsabfrage
* SPACE 
    - Fokussiert das Eingabefeld
* I 
    - Fokussiert den Inventar Tab in der Seitenleiste
* L 
    - Fokussiert den Umgebung Tab in der Seitenleiste
* M 
    - Fokussiert den Menü Tab in der Seitenleiste
* PFEILTASTEN 
    - Navigation durch das Interface
* N, S, W, E, U, D 
    - Schnelle Navigation durch die Spielwelt



Interaktive Session
-------------------

Die Session ...

Datenbank
---------

Die Datenbank ...

SpeechPack
----------

Das Sprachpaket ...

Parser
------

Der Parser ...

User Interface
--------------

Das User Interface ...
