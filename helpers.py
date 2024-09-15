# W tym pliku będą mieścić się pomocnicze funkcje
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox
from calculationfunctions import calculate_expression
from graphlayout import GraphLayout
import listelement
import sympy as sp

from PySide6.QtWidgets import QMessageBox, QPushButton

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
                    button.clicked.connect(lambda ch, t=text: addToExpression(parent, t, parent.funcList, mode = 2))

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
                if expression[0] == mathFormulaField.current_graph:
                    # Zaktualizowanie istniejącego wyrażenia
                    expression[1] += text
                    mathFormulaField.current_graph.typeFormula(expression[1])
                    found = True
                    break
            
            if not found:
                # Dodanie nowego wyrażenia, jeśli nie znaleziono odpowiedniego
                new_expression = text
                mathFormulaField.current_graph.typeFormula(new_expression)
                checkbox = mathFormulaField.widgets[1].findChild(QCheckBox)
                parent.current_expressions.append([mathFormulaField.current_graph, new_expression, checkbox])
    else:
        # Dialog, gdy pole nie jest aktywne
        dlg = QMessageBox()
        dlg.setWindowTitle("Nie można użyć klawiatury")
        dlg.setText("Klawiatura jest zablokowana. Aby móc z niej skorzystać, musisz aktywować pole do edycji danej funkcji.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec()

# Usuwanie ostatniego znaku z formuły matematycznej
def removeLastCharacter(parent, mathFormulaField: GraphLayout, mode):
    if mathFormulaField is not None:
        if mode == 1:
            if len(parent.current_expression) > 0:
                parent.current_expression = parent.current_expression[:-1]
                mathFormulaField.typeFormula(parent.current_expression)
        elif mode == 2:
            for expression in parent.current_expressions:
                if expression[0] == mathFormulaField:
                    if len(expression[1]) > 0:
                        expression[1] = expression[1][:-1]
                        mathFormulaField.typeFormula(expression[1])
                    break
    
# Usuwanie całego wyrażenia matematycznego
def removeExpression(parent, mathFormulaField: GraphLayout, mode):
    if mathFormulaField is not None:
        if mode == 1:
            if len(parent.current_expression) > 0:
                parent.current_expression = ""
                mathFormulaField.typeFormula(parent.current_expression)
        elif mode == 2:
            for expression in parent.current_expressions:
                if expression[0] == mathFormulaField:
                    if len(expression[1]) > 0:
                        expression[1] = ""
                        mathFormulaField.typeFormula(expression[1])
                    break

    # if len(parent.current_expression) != 0:
    #     parent.current_expression = ""
    #     parent.mathFormula.typeFormula(parent.current_expression)

# Dodawanie funkcji do listy funkcji
def onPlusClick(parent):
    if(parent.functionScroll.count() < 11):

        # Tworzenie nowej funkcji - forma tekstowa
        full_result = "f(x)" + " = " + "Enter The Function"
        
        # Stworzenie nowego elementu do listy funkcji
        new_function_item = listelement.prepareWidgetFunc(parent.function_number, parent.funcList, full_result)

        # Inkrementacja numeru funkcji
        parent.function_number += 1

        # Dodanie wyrażenia i wyniku do listy funkcji
        parent.funcList.addWidget(new_function_item)

        # Uchwyt pod guzik do edycji funkcji
        editButton = new_function_item.findChildren(QPushButton)[0]

        # Dodanie sygnału do edycji pola z funkcją
        editButton.clicked.connect(lambda: getSelectedGraph(editButton, parent))

        # Dodanie callbacka do elementu listy z checkboxem
        for i in range(1, parent.functionScroll.count()):

            # Bierzemy każdy checkbox z listy
            checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)

            # Każdy checkbox łączymy z sygnałem
            checkbox.stateChanged.connect(
                    lambda state: onFormulaSelected(parent) 
                )
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("Przekroczono dozwolony limit funkcji")
        dlg.setText("Możesz wprowadzić maksymalnie 10 funkcji.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

# Funkcja do wprowadzenia formuły do pola w zakładce z wykresami
def getSelectedGraph(button, parent):
    # Sprawdzamy, czy istnieje aktywny przycisk
    if parent.active_type_formula_button is not None:
        # Upewniamy się, że przycisk nadal istnieje, używając sygnału `destroyed`
        if parent.active_type_formula_button is not None:
            parent.active_type_formula_button.setStyleSheet("")

    # Jeśli kliknięty przycisk to ten sam, który jest już aktywny, usuwamy styl i dezaktywujemy
    if parent.active_type_formula_button == button:
        button.setStyleSheet("")  # Przywrócenie domyślnego stylu
        parent.active_type_formula_button = None  # Żaden przycisk nie jest aktywny
    else:
        # Ustaw nowy aktywny przycisk
        parent.active_type_formula_button = button
        button.setStyleSheet("background-color: #6D6D6D;")  # Podświetlenie klikniętego przycisku
        
        # Ustawienie sygnału `destroyed`, który ustawi zmienną na None, jeśli obiekt zostanie usunięty
        button.destroyed.connect(lambda: setattr(parent, 'active_type_formula_button', None))

    # Funkcja zwraca aktualny wykres
    current_graph = parent.funcList.current_graph
    return current_graph

# Funkcja rysująca wykres w przypadku zaznaczenia checkboxa
def onFormulaSelected(parent):
    # Listy pod wartości stanu checkboxa oraz referencji do danego checkboxa
    checkboxes_check_states = []
    checkboxes = []
    
    # Pętla, w której dodajemy każdego checkboxa z listy
    for i in range(1, parent.functionScroll.count()):
            checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)
            checkboxes.append(checkbox)
            checkboxes_check_states.append(checkbox.checkState())
            
    # Liczymy ilość zaznaczonych checkboxów
    checkboxSelected = checkboxes_check_states.count(Qt.CheckState.Checked)

    # Jeśli liczba checkboxów jest równa 1 to możemy rysować, w przeciwnym wypadku nie możemy
    parent.active_graph = allowDrawingGraph(checkboxSelected)

    # Jeśli możemy rysować to szukamy zaznaczonego checkboxa, aby móc potem sprzężyć go z odpowiednią funkcją do rysowania
    if(parent.active_graph):
        parent.selected_checkbox = findFirstCheckedCheckbox(checkboxes)

# Funkcja sprawdzająca czy liczba zaznaczonych checkboxów jest równa 1 - w przeciwnym wypadku nie rysujemy funkcji
def allowDrawingGraph(checkboxSelected):
    if(checkboxSelected != 1):
        return False
    return True

# Metoda do rysowanie wybranej funkcji
def drawActiveGraph(parent):
    if(parent.active_graph):

        expression_str = ""
        
        for expression in (parent.current_expressions):
            if parent.selected_checkbox == expression[2]:
                expression_str = expression[1]
                break
            
        parent.graphDisplay.ax.clear()
          
        # Symboliczna zmienna 'x'
        sympy_var = sp.symbols('x')
        
        try:
            # Konwersja napisu na wyrażenie sympy
            sympy_fun = sp.sympify(expression_str)
            
            # Rysowanie wykresu
            parent.graphDisplay.setPlot(sympy_var, sympy_fun, color='red')
        except Exception as e:
            dlg = QMessageBox()
            dlg.setWindowTitle("Błędnie wprowadzona formuła")
            dlg.setText("Wprowadź poprawną formułę do odpowiedniego pola.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            button = dlg.exec()
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("Nie wybrano funkcji do rysowania")
        dlg.setText("Aby narysować funkcję na wykresie należy zaznaczyć JEDNĄ formułę.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

# Funkcja zwraca pierwszy zaznaczony checkbox
def findFirstCheckedCheckbox(checkbox_list):
    for checkbox in checkbox_list:
        if checkbox.checkState() == Qt.CheckState.Checked:
            return checkbox
    return None  # W przypadku, gdy żaden nie jest zaznaczony
            
   
    

