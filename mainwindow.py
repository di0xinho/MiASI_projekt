# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
import importlib as imp

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from helpers import onEqualClick

# for debugging
import time

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Jak narazie pozostawię tą zmienną i wywołanie funkcji w tym pliku - raczej trzeba będzie to przenieść gdzieś indziej
        self.current_expression = "" # Dodajemy atrybut do przechowywania aktualnego wyrażenia
        self.setupButtons()
        #for sleepy in range(10):
        #    time.sleep(3)
        print('x:', self.ui.graphDisplay.ax.get_xlim())
        #self.ui.graphDisplay.ax.callbacks.connect('xlim_changed', lambda event: print('x:', self.ui.graphDisplay.ax.get_xlim()))
        self.ui.graphDisplay.ax.callbacks.connect('xlim_changed', lambda event: self.ui.graphDisplay.redrawPlot())

        # Dodajemy obsługę kliknięcia przycisku "="
        self.ui.tab1Buttons['='].clicked.connect(lambda: onEqualClick(self, parent))
        # Obsługa kliknięcia przycisku usuwającego ostatni znak
        self.ui.tab1Buttons['Usuń ostatni znak'].clicked.connect(self.removeLastCharacter)
        # Obsługa kliknięcia przycisku usuwającego całe wyrażenie matematyczne
        self.ui.tab1Buttons['Usuń całe wyrażenie'].clicked.connect(self.removeExpression)

    # Funkcja obsługująca dodawanie do wyrażenia matematycznego odpowiednie formuły matematyczne przypisane do guzików
    def setupButtons(self):
        for text, button in self.ui.tab1Buttons.items():
            if text not in ['=', 'Usuń ostatni znak', 'Usuń całe wyrażenie']:
                button.clicked.connect(lambda ch, t=text: self.addToExpression(t))
    
    # Dodawanie do wyrażenia odpowiednich formuł matematycznych
    def addToExpression(self, text):
        self.current_expression += text
        self.ui.mathFormula.typeFormula(self.current_expression)

    # Usuwanie ostatniego znaku z formuły matematycznej
    def removeLastCharacter(self):
        if len(self.current_expression) > 0:
            self.current_expression = self.current_expression[:-1]
            self.ui.mathFormula.typeFormula(self.current_expression)
            print("Usuwam")

    # Usuwanie całego wyrażenia matematycznego
    def removeExpression(self):
        if len(self.current_expression) != 0:
            self.current_expression = ""
            self.ui.mathFormula.typeFormula(self.current_expression)

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
