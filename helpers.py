# W tym pliku będą mieścić się pomocnicze funkcje

from calculationfunctions import calculate_expression

# Funkcja obsługująca kliknięcie przycisku "="
def onEqualClick(parent, expression):
    try:
        # print(f"{parent.mathFormula.typeFormula("5+5")}")
        # print(f"{parent.mathFormula.ax.text}")
        vars = {'x': 1, 'y': 2}
        result, latex_expression = calculate_expression(expression, vars)
        print(result)
    except Exception as e:
        parent.answerFormula.setNormalText("Error")


