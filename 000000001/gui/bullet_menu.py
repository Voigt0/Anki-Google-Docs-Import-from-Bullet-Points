from aqt.qt import QMenu
from .anki_menu import get_voigt_menu

def setup_menu() -> QMenu:
    anki_menu = get_voigt_menu()
    result = QMenu("Bullet Point Decks")
    anki_menu.addMenu(result)
    return result
