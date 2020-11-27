Spielobjekte
============
Ein Spielobjekt stellt den kleinsten Baustein eines PyBox Projektes dar. Da PyBox grundlegend auf der Verwendung einer `ZODB` basiert, ist :class:`GameObject` als eine direkte Subklasse von :class:`Persistent` implementiert. Dies ermöglicht es, Instanzen dieses Objekts in der :class:`PyBoxDB` zu speichern und im Spielverlauf auf diese zuzugreifen. 

:badge-blue:`Designparadigma` **GameObjects**

    :class:`GameObject` stellt die Basisklasse aller persistenten Spielobjekte dar und implementieren alle grundlegenden Attribute und Methoden zur Datenbankanbindung, sowie zur Interaktion zwischen Anwender und Applikation.

Da :class:`GameObjects <GameObject>` persistente Objekte sind, gelten gewisse Regeln, welche durch die Basisklasse :class:`Persistent` vorgegeben sind und zwingend bei der implementation jedes Features zu beachten sind.

.. admonition:: persistente Attribute und Methoden

    Um eine korrekte Funktionsweise der Datenbank zu gewährleisten, erfüllen Attribute der Basisklasse :class:`GameObject` eine der folgenden Anforderungen:

        * Sie sind selbst eine Subklasse von :class:`Persistent`
        * Sie sind vom Typ :class:`Immutable`
    
    Mit :class:`PersistentList` sowie :class:`PersistentMapping` stellt :mod:`persistent`, persistente Implementationen von :class:`list` und :class:`dict` bereit. Um komplexere Datenstrukturen zu realisieren können :mod:`Btrees` verwendet werden.

    Sollte die Implementation eines Features die Verwendung von Daten erfordern, die keine der oben genannten Voraussetzungen erfüllen, muss das Attribut :attr:`GameObject._p_changed` manuell gesetzt werden, falls nicht persistente Daten geändert werden.

Das Standardinterface
---------------------
Die Basisklasse :class:`GameObject` stellt ein Standardinterface zur Verfügung, welches die minimalen Anforderungen an interaktive Objekte innerhalb der Engine implementiert.

.. data:: alias
    :type: str

    `object.alias` wird zur eindeutigen Identifikation einer bestimmten Instanz von :class:`GameObject` verwendet. Beispielsweise kann ein Bücherregal zwanzig Instanzen von :class:`Book(GameObject)` enthalten, die in der Textausgabe alle als 'Buch' bezeichnet werden, deren `alias` aber jeweils einzigartig ist.

    Dieses Attribut ist außerdem der Ansatzpunkt für den :class:`Parser`. Eine Spielereingabe wie z.B. 'öffne die Haustür mit dem rostigen Schlüssel' würde durch den Parser in einen Token der Form `{do:'open','obj':'door1',tool:'rustKey'}` umgewandelt, wobei `door1` und `rustKey` für den `alias` eines GameObject stehen.

Szenen - :class:`Scene`
-----------------------
Szenen bilden die Grundbausteine einer Spielwelt.
