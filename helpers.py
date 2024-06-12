# W tym pliku będą mieścić się pomocnicze funkcje

from calculationfunctions import calculate_expression

# Funkcja obsługująca kliknięcie przycisku "="
def onEqualClick(parent):
    try:
        print("Kliknięto =")
    except Exception as e:
        parent.answerFormula.setNormalText("Error")

