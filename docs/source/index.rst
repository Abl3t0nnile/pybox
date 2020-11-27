.. PyBox documentation master file, created by
   sphinx-quickstart on Fri Nov  6 11:37:12 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/header.png
    :alt: PyBox: A simple Text Adventure Engine written in Python.
    :align: center


Willkommen zur Dokumentation der PyBox Engine
=============================================

PyBox ist ein Software Framework zum erstellen interaktiver Text Adventures.

PyBox bietet ein einfaches, aber vielseitiges Set von Tools um Projekte mit der Engine zu erstellen. Die Engine basiert dazu auf einer Weltsimulation, die sich um viele der Interaktionsmöglichkeiten kümmert, ohne das sich Entwickler Gedanken darüber machen müssten. 

Neben dem Editor bietet das Framework eine Laufzeitumgebung, welche in der Lage ist PyBox Projekte zu interpretieren und in einer interaktiven Umgebung spielbar zu machen. Dazu bietet PyBox eine Datenbank, die auf persistenten Objekten basiert und mittels des `ZODB`_ Frameworks implementiert ist, einen intelligenten und mächtigen Parser, der in der Lage ist dynamische Antworten zu generieren, sowie ein User Interface welches das `urwid`_ Paket nutzt.

Somit ist PyBox eine All-in-One Lösung für Text Adventures. Vom Reißbrett bis zum fertigen Spiel.

.. _`ZODB`: http://www.zodb.org/en/latest/
.. _`urwid`: http://urwid.org/

PyBox Guide
-----------

Dieser Guide beschäftigt sich mit der Anwendung des PyBox Frameworks. Er bietet eine schrittweise Einführung in die verschiedenen Features und Konzepte der Engine und vermittelt dabei das notwendige Wissen, um eigene Spiele mit der Engine zu erstellen.


Engine Features und Komponenten
-------------------------------

Dieser Abschnitt beschreibt die Funktionsweise der Engine und legt die genauen Spezifikationen fest. Hier finden sich genaue Abhandlungen über einzelne Aspekte und Grundlagen auf denen die Engine und die Simulation hinter PyBox basieren. Wer verstehen möchte wie PyBox funktioniert ist hier richtig aufgehoben.

.. toctree::
    :maxdepth: 2

    game_objects


API Referenz
------------

Dieser Teil der Dokumentation enthält die `sphinx.autodoc`. Wer also schnell nach einer bestimmten Funktion oder Klasse sucht, sollte hier fündig werden.

.. toctree::
    :maxdepth: 2

    api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
