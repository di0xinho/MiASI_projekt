# W tym pliku będą mieścić się pomocnicze funkcje

from calculationfunctions import calculate_expression

# Funkcja obsługująca kliknięcie przycisku "="
def onEqualClick(self, parent):
    try:
        # print(f"{parent.mathFormula.typeFormula("5+5")}")
        # print(f"{parent.mathFormula.ax.text}")
        vars = {'x': 1, 'y': 2}
        result, latex_expression = calculate_expression(self.current_expression, vars)
        self.ui.answerFormula.typeFormula(result, 5)
        print(result)
    except Exception as e:
        parent.answerFormula.setNormalText("Error")


