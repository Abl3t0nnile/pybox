PyBox Feature Liste
===================
Dieses Dokument gibt ein Übersicht über alle Features der PyBox Engine, sowie deren Implementierungsstand.

Gameplay Features
-----------------
Features dieser Kategorie zählen zu den Programminteraktionen. Diese Features bilden den obersten Abstraktionsgrad der Engine ab und können vom Anwender genutzt werden. In der Regel werden diese Features über eine einzelne Funktion implementiert.

:badge:`todo` **Bewegung in der Spielwelt**

    In PyBox ist es möglich die Spielfigur oder andere bewegliche Objekte zu Bewegen. Dabei befindet sich ein Objekt zu beginn einer Bewegung in einer bestimmten Szene der Spielkarte und verändert seine Position unter Beachtung der möglichen Ausgänge einer Szene.

    Bewegungen sind in den Vier Haupthimmelsrichtungen Norden, Süden, Westen und Osten, sowie nach Oben und Unten möglich. Die Kurzbezeichnung der Richtungen bassiert auf den englischen Vokabeln ([n]orth, [s]outh, [w]est, [e]ast, [u]p, [d]own).

:badge:`todo` **In der Umgebung umsehen**

    Der Spieler kann sich zu jeder Zeit umsehen. Dies gibt eine Beschreibung der aktuellen Szene aus. Dabei handelt es sich in der Regel um einen vordefoinierten Text, welcher aus der Textdatenbank abgerufen wird.

:badge:`todo` **Objekte betrachten**

    Der Spieler kann jedes Objekt innerhalb seines Handlungshorizontes betrachten. Das Programm gibt dann einen Beschreibungstext des addressierten Objektes aus. Dieser wird in der Regel aus der Textdatenbank des Projektes abgerufen, kann aber auch dynamisch erzeugt werden.