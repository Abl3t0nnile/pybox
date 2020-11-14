"""
PyBox
-----

Das ist der Toop Level Doc String des PyBox Pakets.

PyBox ist ein Softwareframework zum erstellen interaktiver Textabenteuer. Es vereint alle notwendingen Tools um solche Programme zu erstellen, zu pflegen und sie abzuspielen.

Um eine möglichst leichte Erweiterbarkeit des Frameworks zu gewährleisten, setzt PyBox auf ein stark modularisiertes System, bei dem jede Programmkomponente sehr spezifische Aufgaben erfüllt.

Eine minimale PyBox Applikation::

    >>> from prybox import PyBoxApplication, Session
    >>> session = Session()
    >>> app = PyBoxApplication(session)
    >>> app.run()
"""