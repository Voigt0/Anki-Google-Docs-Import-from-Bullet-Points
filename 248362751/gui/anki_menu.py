from aqt import mw
from aqt.qt import QMenu

def get_voigt_menu() -> QMenu:
    menubar = mw.form.menubar
    menu_name = "&Voigt"
    for action in menubar.actions():
        if action.text() == menu_name:
            return action.menu()
    return menubar.addMenu(menu_name)
