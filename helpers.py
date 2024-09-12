# W tym pliku będą mieścić się pomocnicze funkcje
from calculationfunctions import calculate_expression

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

# Funkcja obsługująca kliknięcie przycisku "="
def onEqualClick(parent):
    try:
        vars = {'x': 1, 'y': 1}
        result, latex_expression = calculate_expression(parent.current_expression, vars)
        print(result)
        parent.answerFormula.typeFormula(result)
        # parent.addToHistory(parent.current_expression, result)
    except Exception as e:
        dlg = QMessageBox(parent)
        dlg.setWindowTitle("Niepoprawna formuła matematyczna")
        dlg.setText("Wprowadzono niepoprawny format wyrażenia matematycznego. Spróbuj poprawić formułę, aby zwrócić prawidłowy wynik.")
        dlg.setStandardButtons(QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Critical)
        button = dlg.exec()

# Funkcja obsługująca dodawanie do wyrażenia matematycznego odpowiednie formuły matematyczne przypisane do guzików
def setupButtons(parent):
    for text, button in parent.tab1Buttons.items():
        if text not in ['=', 'C', 'AC']:
            button.clicked.connect(lambda ch, t=text: addToExpression(parent, t))

# Dodawanie do wyrażenia odpowiednich formuł matematycznych
def addToExpression(parent, text):
    parent.current_expression += text
    parent.mathFormula.typeFormula(parent.current_expression)

# Usuwanie ostatniego znaku z formuły matematycznej
def removeLastCharacter(parent):
    # FIXME when deleting for example cos it removes only s XD
    if len(parent.current_expression) > 0:
        parent.current_expression = parent.current_expression[:-1]
        parent.mathFormula.typeFormula(parent.current_expression)
        print("Usuwam") # remove debug message

# Usuwanie całego wyrażenia matematycznego
def removeExpression(parent):
    if len(parent.current_expression) != 0:
        parent.current_expression = ""
        parent.mathFormula.typeFormula(parent.current_expression)    




