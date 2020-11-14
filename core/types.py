"""
Dieses Modul implementiert PyBox Speziefische Erweiterungen von Standardtypen und andere Engine spezifischen Typen.
"""

from collections import UserList

class SizedList(UserList):
    "Ein Wrapper um eine Standardliste, der eine maximale Listenlänge implementiert."
    def __init__(self, maxSize: int, initList=[]):
        self.maxSize = maxSize
        if len(initList) >= self.maxSize:
            raise ValueError(f'Initial list ist to big for {self}')
        else:
            super(SizedList, self).__init__(initList)
    
    def append(self, value) -> None:
        if len(self) >= self.maxSize:
            raise Warning(f'SizedList Object is full!')
        else:
            super(SizedList, self).append(value)

class Clock:
    
    def __init__(self, h: int, m: int) -> None:
        "Eine einfache implementierung einer 24 h Uhr."
        self._h = h
        self._m = m
        self._d = 1
    
    def set_time(self, h: int, m: int, d=None):
        if h > 23:
            raise ValueError
        else:
            self._h = h
        if m > 59:
            raise ValueError
        else:
            self._m = m
        
        if not d:
            pass
        else:
            self._d = d
    
    @property
    def time(self) -> tuple:
        return (self._h,self._m)
    @property
    def day(self):
        return self._d
    @property
    def hour(self):
        return self._h
    def add_hour(self):
        "Addiert eine Stunde. Falls 24 h überschritten werden, wird der Tag weiter gesetzt und die Stunden berichtigt."
        self._h += 1
        if self._h >= 24:
            self._h -= 24
            self._d += 1
        else:
            pass
    @property
    def minute(self):
        return self._m
    def add_minute(self):
        "Addiert eine Minute. Falls 60 min überschritten werden, wird die Stunde weiter gesetzt."
        self._m += 1
        if self._m >= 60:
            self._m -= 60
            self.add_hour()
        else:
            pass
    def add_minutes(self, val: int):
        "Addiert `val`Minuten auf die Uhr."
        for i in range(val):
            self.add_minute()
    
    def __str__(self) -> str:
        if self._h < 10:
            hour = "0" + str(self._h)
        else:
            hour = str(self._h)
        if self._m < 10:
            minute = "0" + str(self._m)
        else:
            minute = str(self._m)
        
        return hour + ":" + minute
