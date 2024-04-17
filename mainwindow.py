# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
import importlib as imp

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def checklibs():
    pkgs = ['PySide6', 'matplotlib'] # later 'numpy' will join the list
    ihaveall = True
    for p in pkgs:
        try:
            imp.import_module(p)
        except(ImportError):
            print('Nie zainstalowano', p)
            ihaveall = False
    if not ihaveall:
        print('Nalezy je doinstalowac zeby program dzialal, np. za pomoca pip')
        return False
    return True

if __name__ == "__main__":
    if not checklibs():
        sys.exit(1)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
