Design Manifest
===============
Dieses Manifest bildet die Designgrundlage des gesamten Frameworks und etabliert somit den Scope des Projekts. Im folgenden Text werden Annahmen über die reale Welt getroffen und daraus Designprinzipien sowie Funktionsweise und Features der Engine abgeleitet.

Die Interaktion mit der Spielwelt geschieht in PyBox zugbasiert und nicht in Echtzeit.

Der Spieler kann sich in die vier Haupthimmelsrichtungen Norden, Süden, Westen und Osten, sowie nach Oben und Unten bewegen.

Eine Szene bildet in PyBox einen abgekapselten Handlungsspielraum ab, welcher den grundlegenden Baustein einer Spielwelt verkörpert. Das einfachste Beispiel für eine typische Szene ist ein Raum in einem Haus. Befindet sich der Spieler in einem solchen Raum, so kann er mit allen Gegenständen oder Lebewesen dort interagieren und andere, angrenzende Räume betreten. Da die Orientierung in PyBox ausschließlich in 6 Richtungen funktioniert, lässt sich ein Raum am besten als Würfel visualisieren, auf dessen Innenflächen die vier Wände, die Decke und der Boden projiziert werden. Jede der 6 Seiten kann eine direkte Verbindung zu einer anderen Szene haben.

.. note::

    Eine Szene hat 6 Projektionsflächen, wobei jede dieser Flächen eine direkte Verbindung zu einer anderen Szene haben kann.

Ob es sich bei der Szene nun um einen sprichwörtlichen Raum oder einen Ort im Freien handelt spielt keine Rolle.

















