# W tym pliku będą mieścić się pomocnicze funkcje
from calculationfunctions import calculate_expression

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

# Funkcja obsługująca kliknięcie przycisku "="
def onEqualClick(self, parent):
    try:
        # print(f"{parent.mathFormula.typeFormula("5+5")}")
        # print(f"{parent.mathFormula.ax.text}")
        vars = {'x': 1, 'y': 1}
        result, latex_expression = calculate_expression(self.current_expression, vars)
        self.ui.answerFormula.typeFormula(result)
        # self.ui.historyScroll.clear()
        print(result)
    except Exception as e:
        # parent.answerFormula.setNormalText("Error")
        print("Błąd")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Niepoprawna formuła matematyczna")
        dlg.setText("Wprowadzono niepoprawny format wyrażenia matematycznego. Spróbuj poprawić formułę, aby zwrócić prawidłowy wynik.")
        dlg.setStandardButtons(QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Critical)
        button = dlg.exec()



