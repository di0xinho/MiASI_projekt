# W tym pliku będą mieścić się pomocnicze funkcje
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox
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
        print(result)
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

# Funkcja rysująca wykres w przypadku zaznaczenia checkboxa
def onFormulaSelected(parent, checked, formula):
    if checked:
        parent.graphDisplay.ax.clear()
        parent.graphDisplay.setPlot(sp.symbols('x'), formula)

    checkboxes = []

    for i in range(1, parent.functionScroll.count()):
            checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)
            checkboxes.append(checkbox.checkState())

def drawActiveGraph(parent):
    if(parent.active_graph):
        x = sp.symbols('x')
        parent.graphDisplay.ax.clear()
        parent.graphDisplay.setPlot(x, sp.cos(x + 5))
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("Nie wybrano funkcji do rysowania")
        dlg.setText("Należy zaznaczyć odpowiednią funkcję przed jej narysowaniem.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()
    
    

# def handleCheckboxStateChange(parent, checkbox):
#     # Przechodzimy przez wszystkie checkboxy w functionScroll
#     for i in range(1, parent.functionScroll.count()):
#         other_checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)
#         print("Działam")
#         # Jeśli inny checkbox jest zaznaczony i nie jest to checkbox, który właśnie zaznaczono
#         if other_checkbox != checkbox and other_checkbox.checkState() == Qt.CheckState.Checked:
#             # Odznaczamy pozostałe checkboxy
#             other_checkbox.setCheckState(0)
            

# Funkcja do przypisania callbacków do checkboxów
# def setupCheckboxCallbacks(parent):
#     for i in range(1, parent.functionScroll.count()):
#         checkbox = parent.functionScroll.itemWidget(parent.functionScroll.item(i)).findChild(QCheckBox)

#         # Każdy checkbox ma przypisany callback do zmiany swojego stanu
#         checkbox.stateChanged.connect(lambda state, cb=checkbox: handleCheckboxStateChange(parent, cb))
            
   
    

