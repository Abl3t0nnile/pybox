"""
Dieses Modul enthält nützliche Funktionen, die Frameworkübergreifend verwendet werden können und keinem anderen Modul zugeordnet sind.
"""

import json

def equalize_str(s: str) -> str:
    "Wandelt einen String `s` in einen normalisierten String in Kleinbuchstaben und ohne überflüssige Leerzeichen um und gibt diesen aus."
    return s.lower().strip()

def load_json(path: str) -> dict:
    with open(path, newline='') as file:
        return json.load(file)