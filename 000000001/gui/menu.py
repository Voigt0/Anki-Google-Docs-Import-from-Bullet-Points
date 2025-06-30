from aqt.qt import QMenu
from .anki_menu import get_anki_menu

def setup_menu() -> QMenu:
    anki_menu = get_anki_menu()
    result = QMenu("Remote Decks")
    anki_menu.addMenu(result)
    return result
