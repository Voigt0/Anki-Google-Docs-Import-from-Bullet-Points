# anking_menu.py
from aqt import mw
from aqt.qt import QMenu

def get_anki_menu() -> QMenu:
    menu = mw.form.menubar.addMenu("&Voigt")
    return menu