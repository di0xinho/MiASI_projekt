# W tym pliku będą mieścić się pomocnicze funkcje
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QLabel, QHBoxLayout, QVBoxLayout
from calculationfunctions import calculate_expression
from graphlayout import GraphLayout
import listelement
import sympy as sp

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

# Funkcja obsługująca kliknięcie przycisku "="
def onEqualClick(parent):
    try:
        vars = {'x': 1, 'y': 1}
        result, latex_expression = calculate_expression(parent.current_expression, vars)
        parent.answerFormula.typeFormula(result)
        
        # Rozwiązanie równania dodawane do historii, czyli format - "formuła matematyczna = wynik"
        full_result = parent.current_expression + " = " + str(result)

        # Stworzenie nowego elementu historii
        new_history_item = listelement.prepareWidgetHist(0, parent.histList, full_result)

        # Dodanie wyrażenia i wyniku do historii
        parent.histList.addWidget(new_history_item)
        
        # Usuwanie formuły matematycznej z pola wprowadzania wyrażenia po dodaniu do historii 
        removeExpression(parent)

    except Exception as e:
        dlg = QMessageBox()
        dlg.setWindowTitle("Niepoprawna formuła matematyczna")
        dlg.setText("Wprowadzono niepoprawny format wyrażenia matematycznego. Spróbuj poprawić formułę, aby zwrócić prawidłowy wynik.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Critical)
        button = dlg.exec()

# Funkcja obsługująca dodawanie do wyrażenia matematycznego odpowiednie formuły matematyczne przypisane do guzików
def setupButtons(parent, mode):
    if(mode == 1):
        for text, button in parent.tab1Buttons.items():
            if text not in ['=', 'C', 'AC']:
                button.clicked.connect(lambda ch, t=text: addToExpression(parent, t, parent.mathFormula, mode = 1))
    if(mode == 2):
        for text, button in parent.tab2Buttons.items():
                if text not in ['C', 'AC']:
                    button.clicked.connect(lambda ch, t=text: addToExpression(parent, t, parent.funcList.current_graph, mode = 2))

# Dodawanie do wyrażenia odpowiednich formuł matematycznych
def addToExpression(parent, text, mathFormulaField: GraphLayout, mode):
    if mathFormulaField is not None:
        if mode == 1:
            # Tryb 1 - dodawanie do bieżącego wyrażenia
            parent.current_expression += text
            mathFormulaField.typeFormula(parent.current_expression)
        elif mode == 2:
            # Tryb 2 - szukanie odpowiedniego pola w current_expressions
            found = False
            for expression in parent.current_expressions:
                if expression[0] == mathFormulaField:
                    # Zaktualizowanie istniejącego wyrażenia
                    expression[1] += text
                    mathFormulaField.typeFormula(expression[1])
                    found = True
                    print(mathFormulaField)
                    break
            
            if not found:
                # Dodanie nowego wyrażenia, jeśli nie znaleziono odpowiedniego
                new_expression = text
                mathFormulaField.typeFormula(new_expression)
                parent.current_expressions.append([mathFormulaField, new_expression])
    else:
        # Dialog, gdy pole nie jest aktywne
        dlg = QMessageBox()
        dlg.setWindowTitle("Nie można użyć klawiatury")
        dlg.setText("Klawiatura jest zablokowana. Aby móc z niej skorzystać, musisz aktywować pole do edycji danej funkcji.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec()

# Usuwanie ostatniego znaku z formuły matematycznej
def removeLastCharacter(parent):
    # FIXME when deleting for example cos it removes only s XD
    if len(parent.current_expression) > 0:
        parent.current_expression = parent.current_expression[:-1]
        parent.mathFormula.typeFormula(parent.current_expression)

# Usuwanie całego wyrażenia matematycznego
def removeExpression(parent):
    if len(parent.current_expression) != 0:
        parent.current_expression = ""
        parent.mathFormula.typeFormula(parent.current_expression)

# Dodawanie funkcji do listy funkcji
def onPlusClick(parent):
    if(parent.functionScroll.count() < 7):

        # Tworzenie nowej funkcji - forma tekstowa
        # full_result = "f(x)" + " = " + "x^3"
        x = sp.symbols('x')
        full_result = sp.cos(x + 1)

        # Stworzenie nowego elementu do listy funkcji
        new_function_item = listelement.prepareWidgetFunc(parent.function_number, parent.funcList, full_result)

        # Inkrementacja numeru funkcji
        parent.function_number += 1

        # Dodanie wyrażenia i wyniku do listy funkcji
        parent.funcList.addWidget(new_function_item)

        editButton = new_function_item.findChildren(QPushButton)[0]

        editButton.clicked.connect(lambda: getSelectedGraph(editButton, parent))

        # Dodanie callbacka do elementu listy z checkboxem
        for i in range(1, parent.functionScroll.count()):

            checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)

            checkbox.stateChanged.connect(
                    lambda state: onFormulaSelected(parent, state == 2, full_result) # state == 2 - oznacza to zaznaczenie checkboxa
                )
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("Przekroczono dozwolony limit funkcji")
        dlg.setText("Możesz wprowadzić maksymalnie 6 funkcji.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

# Funkcja do wprowadzenia formuły do pola w zakładce z wykresami
def getSelectedGraph(button, parent):
    
    if(parent.active_type_formula_button != None):
        parent.previous_type_formula_button = parent.active_type_formula_button
        parent.previous_type_formula_button.setStyleSheet("")
    
    if(parent.active_type_formula_button == button):
        parent.funcList.current_graph = None
        parent.active_type_formula_button.setStyleSheet("")
        return

    parent.active_type_formula_button = button
    current_graph = parent.funcList.current_graph
    button.setStyleSheet("background-color: #6D6D6D;")

    return current_graph


# Funkcja rysująca wykres w przypadku zaznaczenia checkboxa
def onFormulaSelected(parent, checked, formula):
    checkboxes = []
    
    for i in range(1, parent.functionScroll.count()):
            checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)
            graph_layout = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QHBoxLayout).findChild(QVBoxLayout).findChild(GraphLayout)
            checkboxes.append(checkbox.checkState())

    checkboxSelected = checkboxes.count(Qt.CheckState.Checked)
    parent.active_graph = allowDrawingGraph(checkboxSelected)

# Metoda do rysowanie wybranej funkcji
def drawActiveGraph(parent):
    if(parent.active_graph):
        print("Rysuję")
        parent.graphDisplay.ax.clear()
        # x = sp.symbols('x')
        # parent.graphDisplay.setPlot(x, "x^2")
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("Nie wybrano funkcji do rysowania")
        dlg.setText("Aby narysować funkcję na wykresie należy zaznaczyć JEDNĄ formułę.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()
    
   

# Funkcja sprawdzająca czy liczba zaznaczonych checkboxów jest równa 1 - w przeciwnym wypadku nie rysujemy funkcji
def allowDrawingGraph(checkboxSelected):
    if(checkboxSelected != 1):
        return False
    return True
            
   
    

