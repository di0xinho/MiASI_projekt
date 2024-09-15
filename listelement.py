from constants import MAINFILE
if __name__ == "__main__":
    print(f"\nTo start calculator run {MAINFILE} file.\n")
    exit(0)

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QPushButton, QScrollArea, QHBoxLayout, QVBoxLayout,
	QSizePolicy, QStatusBar, QWidget, QListWidgetItem, QListWidget, QCheckBox)
from graphlayout import GraphLayout
import sympy as sp

# funexample = "f(x) = 38 * 5 / 7 * \pi * \cos(54) - 783314 + 4,5 * 10^{12} + 38 * 5 / 7 * \pi * \cos(54) - 783314 + 4,5 * 10^{12}"
funexample = "x^2"
funbegin = "f(x) = "
histexample = 'result'

# tworzy widget
def prepareWidgetFunc(n, parent_list, result = funexample) -> QWidget:
    """Widget listing function formulas."""
    widget = QWidget()
    layout = QHBoxLayout()
    check = QCheckBox(f"f_{n}")
    grLayout = GraphLayout()
    grLayout.typeFormula(result, 12, 'left', True)
    layout.addWidget(check)
    layout.addWidget(grLayout.graph)

    editButt = QPushButton()
    editButt.setIcon(QIcon("edit_24dp.png"))

    delButt = QPushButton()
    delButt.setIcon(QIcon("delete_24dp.png"))

    # Łączenie przycisku z metodą usuwania widgetu
    delButt.clicked.connect(lambda: parent_list.deleteWidget(widget))

	# Łączenie przycisku z metodą do edycji formuły w widgecie
    editButt.clicked.connect(lambda: parent_list.editWidget(widget, grLayout))
	
    buttLayout = QVBoxLayout()
    buttLayout.addWidget(editButt)
    buttLayout.addWidget(delButt)
    layout.addLayout(buttLayout)
    
    widget.setLayout(layout)
    widget.setMaximumHeight(120)
    return widget


def prepareWidgetHist(n, parent_list, result = histexample) -> QWidget:
    """Widget listing calculation history."""
    widget = QWidget()
    layout = QHBoxLayout()
    grLayout = GraphLayout()
    grLayout.typeFormula(result, 12, 'left', True)
    layout.addWidget(grLayout.graph)

    button = QPushButton()
    button.setIcon(QIcon("delete_24dp.png"))
    
    # Łączenie przycisku z metodą usuwania widgetu
    button.clicked.connect(lambda: parent_list.deleteWidget(widget))

    layout.addWidget(button)
    widget.setLayout(layout)
    widget.setMaximumHeight(120)
    return widget

# TODO align text to left

# lista wyników albo funkcji - historyList, graphList
class GraphList: # misleading name
	"List of graphs. Can be used to display calc history or function formulas"
	def __init__(self, parent, historyMode=False):
		self.list_widget = QListWidget(parent)
		self.history_mode=historyMode
		self.widgets = []
		self.current_graph = None
		self.createButton()

	def createButton(self):
		widget = QWidget()
		layout = QHBoxLayout() # will contain one thing
		button = QPushButton()
		layout.addWidget(button)
		button_2 = QPushButton()
		if self.history_mode:
			button.setText(u'Wyczyść historię')
			button.clicked.connect(self.clearHistory)  # Połącz guzik z funkcją czyszczenia historii
		else:
			button.setIcon(QIcon("add_24dp.png"))
			button_2.setText(u'Rysuj wykres')
			layout.addWidget(button_2)
		
		widget.setLayout(layout)
		self.widgets.append(widget)
		item = QListWidgetItem(self.list_widget)
		item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
		item.setSizeHint(QSize(self.list_widget.sizeHint().width(), 40))
		self.list_widget.setItemWidget(item, widget)
		pass

	# Dodawanie przykładów w postaci funkcji i wyników do historii

	# Funkcje
	def prepareFuncExample(self):
		for i in range(3):
			widget = prepareWidgetFunc(i, self)  # Przekazana instancja GraphList
			self.addWidget(widget)

	# Historia
	def prepareHistExample(self):
		for i in range(3):
			widget = prepareWidgetHist(i, self)  # Przekazana instancja GraphList
			self.addWidget(widget)

	# dodaj element do listy
	def addWidget(self, widget: QWidget):
		insertAt=1
		"Add widget to list in interface. Works for both history and functions"
		self.widgets.insert(insertAt, widget)
		item = QListWidgetItem()
		item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
		item.setSizeHint(QSize(self.list_widget.sizeHint().width(), widget.size().height()))
		self.list_widget.insertItem(insertAt, item)
		self.list_widget.setItemWidget(item, widget)
		pass
	def editWidget(self, widget: QWidget, graph_layout):
		"when listing functions, there is an option to enter edit mode, to edit function"
		self.current_graph = graph_layout
		return True
			
		pass
	def deleteWidget(self, widget: QWidget):
		"Usuwa wybrany widget z listy"
		# Znajdujemy indeks elementu, który odpowiada podanemu widgetowi
		for i in range(self.list_widget.count()):
			item = self.list_widget.item(i)
			if self.list_widget.itemWidget(item) == widget:
				# Usuwamy element z listy
				self.list_widget.takeItem(i)
				self.widgets.remove(widget)  # Usuń widget z listy przechowywanych widgetów
				widget.deleteLater()  # Opcjonalnie, jeśli chcesz usunąć widget całkowicie
				break
			pass

	def clearHistory(self):
		"""Usuwa wszystkie elementy z historii oprócz przycisku, który również znajduje się w tablicy widgetów"""
		# Usuwamy wszystkie elementy z listy zaczynając od 1 (indeks 0 to przycisk)
		for i in range(1, self.list_widget.count()):
			self.list_widget.takeItem(1)  # Usuwa drugi element (indeks 1), bo lista się dynamicznie skraca

		# Usuwamy odpowiadające elementy z listy self.widgets, zostawiając przycisk na pozycji 0
		self.widgets = self.widgets[:1]

	pass

# TODO element listy z wszystkimi feature'ami wypisanymi poniżej

# ✔

# to będzie klasa, która umożliwi wyświetlenie jakiejś formuły mat (wyniki z historii obliczeń / funkcje)
# jako element listy.

# ogólne opcje:
# - wyświetlanie formuły, 1 lub 2
# - stały tekst na początku, jak np. f(x)=
# - możliwość dołożenia przycisków / dropdown
# - opcja usuń

# Usuń, możliwe rozwiązania: Albo prawym i wybrać usuń, albo przycisk z symbolem kosza albo X.
# albo dropdown menu pod prawym przyciskiem, albo przyciski z ikonkami

# te mogą być w oddzielnych dziedziczących z tego klasach:

# opcje historii:
# - kliknij, aby skopiować wynik

# opcje listy wykresów:
# - checkbox - kontroluje widoczność na wykresie. Może zamiast tego wyszarzanie pod lewym przyciskiem myszy?
# - edytuj (button lub w dropdownie)
# - może pole z kolorem?
