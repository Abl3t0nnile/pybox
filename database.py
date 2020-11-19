"""Dieses Modul implementiert die grundlegene Datenstruktur zur Verwaltung persistenter Daten innerhalb der PyBox Engine.

PyBox nutzt eine `ZODB`_ um Objekte persistent zu speichern. Daher müssen alle Objekte, die zur Verwendung mit dieser Datenbank vorgesehen sind `Persistent`_ subklassieren. Zur Organisation der einzelnen Datenbanktabellen kommen `BTrees`_ aus dem *ZOPE Framework* zum Einsatz. Persistente Speichervorgänge werden über `transaktionen <transactions>`_ gelöst.

Für weitere Informationen bezüglich der Funktionsweise des *ZOPE Frameworks* finden sich in der Dokumentation der jeweiligen Pakete.

.. _ZODB: https://github.com/zopefoundation/zodb
.. _Persistent: https://github.com/zopefoundation/persistent
.. _transaction: https://github.com/zopefoundation/transaction
.. _BTrees: https://github.com/zopefoundation/BTrees

"""

import os
import transaction

from .models.game_object import GameObject

from ZODB import DB, FileStorage
from BTrees import OOBTree


class PyBoxDB:
    """PyBox nutzt :mod:`ZODB` um persistente Objekte zu speichern. Daher müssen alle Objekte, die zur Verwendung mit dieser Datanbank vorgesehen sind Subklassen von :class:`persistent.Persistent` sein.
    
    Diese Implementierung eines Datanbank Interfaces stellt lediglich einen einfachen Wrapper um eine ZODB Instanz dar und bietet vor allem Methoden um Engine spezifische Operationen zu vereinfachen.
    
    **Erstellen einer neuen Datenbank**::
        
        >>> from pybox.database import PyBoxDB
        >>> db = PyBoxDB('/path/to/project/folder')
        >>> db.init()
    
    **Datanbankeinträge hinzufügen**::
    
        >>> from pybox.models import GameObject, Scene
        >>> item = GameObject('alias', 'name')
        >>> scene = Scene('alias', 'name')
        >>> db.add_item(item)
        >>> db.add_item(scene, table='scenes')
        >>> db.commit()
    
    """
    def __init__(self, projectPath):
        name = projectPath.split('/')[-1]
        path = projectPath + f'/data/{name}.fs'
        self.__storage = FileStorage.FileStorage(path)
        self.__zodb = DB(self.__storage)
        self.__conn = self.__zodb.open()
        self.__root = self.__conn.root()
    
    def init(self):
        self.__root.scenes = OOBTree.BTree()
        self.__root.assets = OOBTree.BTree()
        self.player = None
        self.commit()
    
    def close(self):
        self.__conn.close()
        self.__zodb.close()
        self.__storage.close()
    
    def _get__root(self) -> object:
        "Read only Property, welches Zugriff auf das Root Objekt der Datenbank gewährt."
        return self.__root
    root = property(_get__root)
    
    def _get_scenes(self) -> OOBTree.BTree:
        "Read only Property, welches Zugriff auf die Szenen Tabelle der Datenbank gewährt."
        return self.__root.scenes
    scenes = property(_get_scenes)
    
    def _get_assets(self) -> OOBTree.BTree:
        "Read only Property, welches Zugriff auf die Asset Tabelle der Datenbank gewährt."
        return self.__root.assets
    assets = property(_get_assets)
    
    def add_item(self, item: object, table='assets') -> None:
        """Fügt ein Instanz eines :class:`GameObject` Objekt zur Datenbank hinzu.
        
        Args:
            table (str): Tabelle in der das Objekt gespeichert werden soll. Default='assets'
        
        Raises:
            KeyError: If `item` ist keine Subklasse von :class:~GameObject`
        
        """
        
        if not isinstance(item, GameObject):
            raise TypeError
        
        key = item.alias
        table = getattr(self, table)
        
        if key in table:
            print(f'Datenbankadresse: "{key}" für Tabelle "{table}" bereits zugewiesen. Soll der Eintrag überschrieben werden? (y/n)')
            choice = None
            while choice not in [True, False]:
                _ = input('> ')
                if _ in ['y', 'Y']:
                    choice = True
                elif _ in ['n', 'N']:
                    choice = False
                else:
                    pass
            if choice:
                print("Datenbankadresse wird überschrieben.")
                pass
            elif not choice:
                print("Schreibvorgang abgegbrochen.")
                return
        else:
            print(f'Neues Objekt unter der Adresse "{key}" eingefügt."')
        
        table[key] = item
    def add_items(self, items: list, table='assets'):
        for item in items:
            self.add_item(item, table)
    
    @staticmethod
    def commit():
        "Kurzbefehl für `transaction.commit`. Aktualisiert alle Datenbankeinträge, die seit dem letzten `commit` verändert wurden."
        transaction.commit()
    @staticmethod
    def abort():
        "Kurzbefehl für `transaction.abort`. Wiederruft alle Änderungen an der Datenbank seit dem letzten `commit`. Die geänderten Daten sind unwiederbringlich verloren."
        transaction.abort()
